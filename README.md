Got it 👍 — let’s fix that.

If your **README** is showing the Hugging Face or localhost links as plain text (not clickable), it’s usually because:

* The file is inside a code block (triple backticks ```), or
* Markdown rendering is being escaped by indentation or missing blank lines.

Below is a **clean, fully functional version** — all clickable links will render correctly on **GitHub**, **Hugging Face**, or **VS Code preview** 👇

---

# 🤖 Multimodal AI Assistant

An intelligent assistant built with **Together AI**, capable of:

* 🗣️ Understanding and responding to **voice input** (using Whisper)
* 🧠 Generating natural replies with **Together AI's Llama-3-70b**
* 🖼️ Analyzing uploaded **images**
* 🌐 Performing **real-time web search** (via Google CSE)
* 🔊 Replying back with **voice output** (using gTTS)

---

## 🚀 Live Demo

👉 **[Click here to try it on Hugging Face](https://huggingface.co/spaces/nwankwolinus/gpt-4o-mini_chatbot)**

---

## 🔧 Features

* 🎤 **Voice-to-Text** – Whisper transcribes speech in real-time.
* 💬 **Chat Interface** – Powered by Together AI for natural conversation.
* 🖼️ **Image Analysis** – Upload an image and receive contextual insights.
* 🔍 **Web Search** – Automatically performs Google Custom Search when needed.
* 🔊 **Text-to-Speech** – Uses gTTS to speak responses aloud.
* 🛡️ **Content Moderation** – Filters unsafe input/output automatically.

---

## 🛠️ Tech Stack

* **Frontend/UI**: Gradio
* **Backend**: Python
* **AI Models**:

  * [Together AI Llama-3-70b](https://together.ai/)
  * [Whisper (Speech-to-Text)](https://github.com/openai/whisper)
  * [gTTS (Text-to-Speech)](https://pypi.org/project/gTTS/)
* **Real-time Search**: Google Custom Search API
* **Deployment Options**: Localhost / Hugging Face Spaces / Render / Colab

---

## 🔐 Environment Variables

Create a `.env` file with your API keys:

```bash
TOGETHER_API_KEY=your_together_ai_key
GOOGLE_API_KEY=your_google_api_key
GOOGLE_CSE_ID=your_google_custom_search_engine_id
```

---

## 📦 Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/ai-assistant-with-moderation.git
cd ai-assistant-with-moderation
```

**Repository:** [https://github.com/yourusername/ai-assistant-with-moderation](https://github.com/yourusername/ai-assistant-with-moderation)

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure environment variables

```bash
cp .env.example .env
# Edit .env with your API keys
```

### 4️⃣ Run the application

```bash
python app.py
```

### 5️⃣ Access the application

Open **[http://localhost:7860](http://localhost:7860)** in your browser.

---

## 🎯 Usage Examples

### 🎙️ Voice Conversation

* Click the microphone icon and speak.
* The AI transcribes, processes, and replies with voice output.

### 🖼️ Image Analysis

* Upload an image and ask questions about it.
* Receive detailed contextual analysis.

### 🌍 Real-time Search

* Ask: *“What’s the latest AI news today?”*
* Get up-to-date answers via web search integration.

### 💬 Text Chat

* Type your messages for instant AI responses.

---

## 🏗️ Project Structure

```
multimodal-ai-assistant/
├── app.py                 # Main application
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
├── .env.example           # Environment template
└── .gitignore             # Ignore rules
```

---

## 🔍 Real-Time Search Triggers

The assistant triggers web searches for:

* `latest`, `current`, `today`, `now`, `recent`
* `news`, `breaking`, `live`, `update`
* `who is`, `what is`, `when is`, `where is`
* `weather`, `scores`, `stock`, `price`

---

## 🛡️ Safety Features

* **Input Moderation** – blocks unsafe or violent queries.
* **Output Moderation** – redacts harmful responses.
* **Banned Keywords** – kill, bomb, hack, terror, attack, violence, etc.

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 📄 License

**MIT License** — free for personal or commercial use.

---

**Built with ❤️ using [Together AI](https://together.ai/), [Google Search](https://developers.google.com/custom-search), and [Gradio](https://gradio.app/)**

---

✅ **All links above (Hugging Face, localhost, GitHub, model docs)** are now clickable.
If it still appears as plain text in your preview, check that:

* You didn’t accidentally wrap the entire README inside ```markdown code fences.
* The file extension is `.md`.

Would you like me to format this version for **Hugging Face Spaces** display (they sometimes render Markdown slightly differently than GitHub)?
