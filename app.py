# === Imports and Configurations ===
import os
import gradio as gr
from together import Together
from gtts import gTTS
import tempfile
from typing import List, Dict, Tuple, Optional
from googleapiclient.discovery import build
import whisper
import base64
from PIL import Image
import io

# === Load Whisper model ===
model = whisper.load_model("base")

# === Load API keys from Hugging Face Secrets ===
together_api_key = os.getenv("TOGETHER_API_KEY")
google_api_key = os.getenv("GOOGLE_API_KEY")
google_cse_id = os.getenv("GOOGLE_CSE_ID")

# === Initialize Together Client ===
client = Together(api_key=together_api_key)

# === System Prompt ===
SYSTEM_PROMPT = """You are a helpful, intelligent assistant with real-time web search capabilities. 
Follow these guidelines:
1. Provide accurate and helpful information
2. Be concise and clear in your responses
3. Use web search results when real-time information is needed
4. Never produce harmful, unethical, or dangerous content
5. If you cannot answer a question appropriately, explain why politely"""

# === Moderation Logic ===
BANNED_KEYWORDS = ["kill", "bomb", "hack", "terror", "attack", "suicide", "murder", "violence", "harm", "dangerous"]

def moderate_input(prompt: str) -> Tuple[bool, str]:
    """Check if user input contains disallowed content."""
    lowered = prompt.lower()
    for word in BANNED_KEYWORDS:
        if word in lowered:
            return False, f"❌ Your input violated the moderation policy. Banned keyword: '{word}'"
    return True, ""

def moderate_output(response: str) -> Tuple[str, bool]:
    """Redact unsafe words in the AI output."""
    moderated = response
    violated = False
    for word in BANNED_KEYWORDS:
        if word in moderated.lower():
            violated = True
            moderated = moderated.replace(word, "[REDACTED]")
            moderated = moderated.replace(word.capitalize(), "[REDACTED]")
    return moderated, violated

# === Real-Time Web Search Function ===
def search_web(query: str) -> str:
    try:
        service = build("customsearch", "v1", developerKey=google_api_key)
        result = service.cse().list(q=query, cx=google_cse_id, num=3).execute()
        items = result.get("items", [])
        if not items:
            return "🔍 No results found for your query."

        formatted_results = []
        for item in items:
            title = item.get("title", "No Title")
            link = item.get("link", "")
            snippet = item.get("snippet", "")
            formatted_results.append(f"**{title}**\n{snippet}\n🔗 {link}")

        return "\n\n".join(formatted_results)

    except Exception as e:
        return f"❌ Error during web search: {e}"

# === Real-Time Search Detection ===
def should_trigger_search(text: str) -> bool:
    """Determine if query needs real-time information"""
    search_keywords = [
        "latest", "current", "recent", "now", "today", "upcoming", 
        "new version", "update", "version number", "release date",
        "as of today", "as of now", "currently", "right now", "present",
        "news", "breaking", "live", "score", "weather", "stock", "price",
        "who is", "what is", "when is", "where is"
    ]
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in search_keywords)

# === Enhanced AI Response Handler with Real-Time Search ===
def generate_response(user_input: str, messages: List[Dict]) -> str:
    # Input moderation
    is_safe, warning = moderate_input(user_input)
    if not is_safe:
        return warning

    try:
        # Check if real-time search is needed
        needs_search = should_trigger_search(user_input)
        search_results = None
        
        if needs_search:
            print(f"[DEBUG] Triggering real-time search for: {user_input}")
            search_results = search_web(user_input)
            
            # If we have valid search results, enhance the prompt
            if not search_results.startswith("❌") and not search_results.startswith("🔍 No results"):
                enhanced_prompt = f"""User question: {user_input}

Recent information from web search:
{search_results}

Please provide a helpful response incorporating this up-to-date information. Be concise and focus on the most relevant details."""
                
                response = client.chat.completions.create(
                    model="meta-llama/Llama-3-70b-chat-hf",
                    messages=messages + [{"role": "user", "content": enhanced_prompt}],
                    max_tokens=1000
                )
            else:
                # If search failed, proceed with original prompt
                response = client.chat.completions.create(
                    model="meta-llama/Llama-3-70b-chat-hf",
                    messages=messages + [{"role": "user", "content": user_input}],
                    max_tokens=1000
                )
        else:
            # Normal response without search
            response = client.chat.completions.create(
                model="meta-llama/Llama-3-70b-chat-hf",
                messages=messages + [{"role": "user", "content": user_input}],
                max_tokens=1000
            )
        
        reply = response.choices[0].message.content.strip()

        # Output moderation
        moderated_reply, violated = moderate_output(reply)
        if violated:
            final_response = "⚠️ The AI's response contained unsafe content and was redacted:\n\n" + moderated_reply
        else:
            final_response = moderated_reply
        
        # Add search attribution if used
        if needs_search and search_results and not search_results.startswith("❌"):
            final_response += f"\n\n🔍 *Information sourced from real-time web search*"
            
        return final_response

    except Exception as e:
        return f"Error generating response: {e}"

# === Simple Image Analysis Handler ===
def analyze_image(image_data: str, prompt: str) -> str:
    """Simple image analysis - describe basic image properties"""
    try:
        if isinstance(image_data, str) and os.path.exists(image_data):
            # Basic image analysis without AI vision
            with Image.open(image_data) as img:
                width, height = img.size
                format_type = img.format
                mode = img.mode
                
                basic_info = f"📷 **Image Information:**\n"
                basic_info += f"• Dimensions: {width} x {height} pixels\n"
                basic_info += f"• Format: {format_type}\n"
                basic_info += f"• Color Mode: {mode}\n\n"
                
                if prompt.lower() in ["describe this image", "what is in this image", "please describe this image"]:
                    return basic_info + "🔍 *For detailed image analysis, please use an AI service that supports vision capabilities.*"
                else:
                    return basic_info + f"💡 *You asked: '{prompt}'\n\nFor detailed image analysis, please use an AI service that supports vision capabilities.*"
        else:
            return "❌ Invalid image file provided."
            
    except Exception as e:
        return f"❌ Image analysis error: {str(e)}"

# === Enhanced Chat Interface Handler ===
def chat_interface(
    user_input: str,
    history: List[Dict],
    image: Optional[str] = None,
    voice: Optional[str] = None
) -> Tuple[List[Dict], str, Optional[str], Optional[str], Optional[str]]:

    if history is None:
        history = []

    audio_path = None
    transcribed_input = None

    # Handle voice input
    if voice:
        try:
            print("[DEBUG] Transcribing voice input...")
            result = model.transcribe(voice)
            transcribed_input = result.get("text", "").strip()
            print(f"[DEBUG] Transcribed: {transcribed_input}")
            user_input = transcribed_input
            history.append({"role": "user", "content": user_input})
        except Exception as e:
            print("[ERROR] Failed to transcribe audio:", e)
            history.append({"role": "user", "content": "Sorry, I couldn't process that audio"})

    # Handle text input
    elif user_input.strip():
        history.append({"role": "user", "content": user_input})
    else:
        # Handle image-only input
        if image:
            user_input = "Please describe this image"
            history.append({"role": "user", "content": user_input})
        else:
            return history, "", image, voice, None  # Empty input fallback

    # Build message context for AI
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages.extend([msg for msg in history if msg["role"] in ["user", "assistant"]])

    # Handle image input (basic analysis only)
    if image:
        try:
            print("[DEBUG] Analyzing image (basic)...")
            img_prompt = user_input if user_input.strip() else "Please describe this image"
            analysis = analyze_image(image, img_prompt)
            history.append({"role": "assistant", "content": analysis})
        except Exception as e:
            print("[ERROR] Image analysis failed:", e)
            history.append({"role": "assistant", "content": f"❌ Failed to analyze image: {e}"})

    # Generate AI reply (skip if we only did image analysis)
    if user_input.strip() or not image:  # Only generate if there's text input or no image
        ai_reply = generate_response(user_input, messages)
        history.append({"role": "assistant", "content": ai_reply})

    # Voice Output (TTS)
    if voice and history:
        try:
            # Get the latest assistant response
            latest_assistant_msg = None
            for msg in reversed(history):
                if msg["role"] == "assistant":
                    latest_assistant_msg = msg["content"]
                    break
            
            if latest_assistant_msg:
                tts = gTTS(text=latest_assistant_msg)
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmpfile:
                    tts.save(tmpfile.name)
                    audio_path = tmpfile.name
        except Exception as e:
            print("[ERROR] TTS generation failed:", e)
            audio_path = None

    return history, "", None, None, audio_path

# === Fixed Gradio UI Layout ===
with gr.Blocks(theme=gr.themes.Soft(), title="AI Assistant with Moderation & Real-Time Search") as demo:
    gr.Markdown("""
    # 🤖 AI Assistant with Voice, Web Search & Moderation
    
    **✨ Features:**
    - ✅ **Input/Output Moderation** - Banned keywords filtered
    - ✅ **Real-Time Google Search** - Automatic search for current information
    - ✅ **Basic Image Info** - Basic image properties analysis
    - ✅ **Voice I/O** - Speak and listen to responses
    - ✅ **Safety First** - Content moderation at both stages
    
    **🔍 Real-Time Search Triggers**: latest, current, today, news, weather, scores, etc.
    **📷 Image Support**: Basic image information (dimensions, format, etc.)
    """)

    chatbot = gr.Chatbot(
        height=500, 
        show_label=False, 
        show_copy_button=True,
        type="messages"
    )
    
    with gr.Row():
        msg = gr.Textbox(
            placeholder="Type your message here... Ask about current events for real-time search!",
            container=False, 
            scale=4
        )
        send_btn = gr.Button("Send", variant="primary", scale=1)
    
    with gr.Row():
        image_input = gr.Image(
            type="filepath", 
            label="📷 Upload Image (Basic Info Only)"
        )
        voice_input = gr.Audio(
            type="filepath", 
            label="🎤 Speak"
        )
    
    audio_output = gr.Audio(
        label="🔊 AI Response", 
        autoplay=True, 
        visible=False
    )
    
    with gr.Row():
        clear_btn = gr.Button("🗑️ Clear Chat")
        test_search_btn = gr.Button("🔍 Test Real-Time Search")
    
    state = gr.State([])

    # Test search button
    def test_search():
        return "What are the latest technology news today?"
    
    test_search_btn.click(
        fn=test_search,
        outputs=[msg]
    )

    send_btn.click(
        fn=chat_interface,
        inputs=[msg, state, image_input, voice_input],
        outputs=[chatbot, msg, image_input, voice_input, audio_output]
    )

    voice_input.change(
        fn=chat_interface,
        inputs=[msg, state, image_input, voice_input],
        outputs=[chatbot, msg, image_input, voice_input, audio_output]
    )

    clear_btn.click(
        fn=lambda: ([], "", None, None, None),
        outputs=[chatbot, state, msg, image_input, audio_output]
    )

# === Launch App ===
if __name__ == "__main__":
    print("🚀 Starting AI Assistant with Moderation & Real-Time Search...")
    print("✅ Together AI Integration Active")
    print("✅ Google Search Ready")
    print("✅ Moderation System Enabled")
    print("📷 Basic Image Analysis Available")
    demo.launch(server_name="0.0.0.0", server_port=7860)