Here’s your **complete and polished `README.md`**, fully merged and with all URLs made clickable and properly formatted for GitHub or Hugging Face display 👇

---

````markdown
# 🤖 Multimodal AI Assistant

An intelligent assistant built with **Together AI**, capable of:

- 🗣️ Understanding and responding to **voice input** (using Whisper)
- 🧠 Generating natural replies with **Together AI's Llama-3-70b**
- 🖼️ Analyzing uploaded **images**
- 🌐 Performing **real-time web search** (via Google CSE)
- 🔊 Replying back with **voice output** (using gTTS)

---

## 🚀 Live Demo

👉 [**Click here to try it on Hugging Face**](https://huggingface.co/spaces/nwankwolinus/gpt-4o-mini_chatbot)

---

## 🔧 Features

- 🎤 **Voice-to-Text**: Users can speak, and Whisper will transcribe the speech in real-time.  
- 💬 **Chat Interface**: Powered by Together AI for fluent, natural conversation.  
- 🖼️ **Image Analysis**: Upload an image and receive contextual visual analysis.  
- 🔍 **Web Search**: Automatically detects when current data is needed and performs a web search using Google Custom Search API.  
- 🔊 **Text-to-Speech**: AI responses are read aloud using Google Text-to-Speech (gTTS).  
- 🛡️ **Content Moderation**: Built-in input/output filtering for safety.  

---

## 🛠️ Tech Stack

- **Frontend/UI**: Gradio  
- **Backend**: Python  
- **AI Models**:  
  - [Together AI Llama-3-70b](https://together.ai/)  
  - [Whisper (Speech-to-Text)](https://github.com/openai/whisper)  
  - [gTTS (Text-to-Speech)](https://pypi.org/project/gTTS/)  
- **Real-time Search**: Google Custom Search API  
- **Deployment Options**: Localhost / Hugging Face Spaces / Render / Colab  

---

## 🔐 Environment Variables

Create a `.env` file or use secret manager with the following keys:

```bash
TOGETHER_API_KEY=your_together_ai_key
GOOGLE_API_KEY=your_google_api_key
GOOGLE_CSE_ID=your_google_custom_search_engine_id
````

---

## 📦 Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/ai-assistant-with-moderation.git
   cd ai-assistant-with-moderation
   ```

   📁 Repository: [https://github.com/yourusername/ai-assistant-with-moderation](https://github.com/yourusername/ai-assistant-with-moderation)

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**

   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

4. **Run the application**

   ```bash
   python app.py
   ```

5. **Access the application**

   Open [http://localhost:7860](http://localhost:7860) in your browser.

---

## 🎯 Usage Examples

### 🎙️ Voice Conversation

* Click the microphone icon and speak your question.
* AI will transcribe, process, and respond with voice output.

### 🖼️ Image Analysis

* Upload an image and ask questions about it.
* Get detailed analysis and descriptions.

### 🌍 Real-time Search

* Ask about current events like: *“What’s the latest tech news?”*
* Get up-to-date information with web search integration.

### 💬 Text Chat

* Type your questions for instant AI responses.

---

## 🏗️ Project Structure

```
multimodal-ai-assistant/
├── app.py                 # Main application
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── .env.example           # Environment template
└── .gitignore             # Git ignore rules
```

---

## 🔍 Real-Time Search Triggers

The assistant automatically performs web searches for:

* `latest`, `current`, `today`, `now`, `recent`
* `news`, `breaking`, `live`, `update`
* `who is`, `what is`, `when is`, `where is`
* `weather`, `scores`, `stock`, `price`

---

## 🛡️ Safety Features

* **Input Moderation**: Blocks queries with harmful keywords.
* **Output Moderation**: Redacts unsafe content in responses.
* **Banned Keywords**: kill, bomb, hack, terror, attack, violence, etc.

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

## 📄 License

**MIT License** — feel free to use this project for personal or commercial purposes.

---

**Built with ❤️ using [Together AI](https://together.ai/), [Google Search](https://developers.google.com/custom-search), and [Gradio](https://gradio.app/)**

```

---

✅ **Highlights of this version:**
- All URLs are now **clickable**
- Markdown fully compatible with GitHub, Hugging Face, and VS Code
- Consistent emoji headers for better readability
- Professionally formatted with horizontal rules (`---`) between sections

Would you like me to format this into a **GitHub-style rich preview (HTML-rendered)** version next — so you can visualize how it’ll look before uploading?
```
