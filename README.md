## README.md 

```markdown
# 🤖 AI Assistant with Moderation & Real-Time Search

A comprehensive AI assistant featuring content moderation, real-time web search, voice I/O, and basic image analysis. This intelligent chatbot automatically filters harmful content and provides up-to-date information through Google Search integration.

## ✨ Features

- ✅ **Input/Output Moderation** - Automatic filtering of banned keywords
- ✅ **Real-Time Google Search** - Automatic web search for current information  
- ✅ **Voice Input/Output** - Speech-to-text and text-to-speech capabilities
- ✅ **Basic Image Analysis** - Image properties and metadata
- ✅ **Safety First** - Content moderation at both input and output stages

## 🚀 Demo

Try the live demo on Hugging Face Spaces:  
👉 [https://huggingface.co/spaces/nwankwolinus/gpt-4o-mini_chatbot](https://huggingface.co/spaces/nwankwolinus/gpt-4o-mini_chatbot)

## 🛡️ Moderation Features

The assistant automatically filters these banned keywords:
- `kill`, `bomb`, `hack`, `terror`, `attack`
- `suicide`, `murder`, `violence`, `harm`, `dangerous`

Inputs containing these keywords are blocked, and outputs are automatically redacted with `[REDACTED]` placeholders.

## 🔍 Real-Time Search

Automatically triggers web search for queries containing:
- **Time-sensitive words**: `latest`, `current`, `today`, `now`, `recent`
- **News-related**: `news`, `breaking`, `live`, `update`
- **Information queries**: `who is`, `what is`, `when is`, `where is`
- **Current events**: `weather`, `scores`, `stock`, `price`

## 🎤 Voice Features

- **Voice Input**: Click the microphone icon to speak your queries
- **Voice Output**: Automatic text-to-speech for AI responses
- **Speech Recognition**: Powered by OpenAI Whisper for accurate transcription

## 📷 Image Support

Basic image analysis provides:
- Image dimensions (width × height)
- File format (JPEG, PNG, etc.)
- Color mode (RGB, Grayscale, etc.)
- Basic metadata information
```

## README.md (Part 2/2)

```markdown
## 🏗️ Architecture

- **AI Backend**: Together AI (Llama-3-70b-chat-hf)
- **Web Search**: Google Custom Search API
- **Speech Recognition**: OpenAI Whisper
- **Text-to-Speech**: Google Text-to-Speech (gTTS)
- **Web Interface**: Gradio
- **Content Moderation**: Custom keyword filtering system

## 🔧 Setup & Installation

### Prerequisites

- Python 3.8+
- API keys for:
  - [Together AI](https://together.ai/)
  - [Google Custom Search API](https://developers.google.com/custom-search/v1/introduction)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-assistant-with-moderation.git
   cd ai-assistant-with-moderation
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` with your API keys:
   ```env
   TOGETHER_API_KEY=your_together_api_key_here
   GOOGLE_API_KEY=your_google_api_key_here
   GOOGLE_CSE_ID=your_google_cse_id_here
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:7860`

## 📁 Project Structure

```
ai-assistant-with-moderation/
├── app.py              # Main application
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
├── .env.example       # Environment variables template
└── .gitignore         # Git ignore rules
```

## 🎯 Usage Examples

### Text Conversations
```
User: "What are the latest technology news?"
AI: Provides current tech news with real-time search results
```

### Voice Interactions
```
User: [Speaks] "What's the weather like today?"
AI: [Speaks response] Provides current weather information
```

### Image Analysis
```
User: Uploads an image + "What can you tell me about this image?"
AI: Provides image dimensions, format, and basic information
```

### Moderation Examples
```
User: "How to make a bomb?" 
AI: "❌ Your input violated the moderation policy. Banned keyword: 'bomb'"
```

## 🐛 Troubleshooting

### Common Issues

1. **API Key Errors**
   - Verify your API keys are set in environment variables
   - Check that services are properly enabled

2. **Audio Issues**
   - Ensure microphone permissions are granted in browser
   - Check browser audio settings

3. **Search Not Working**
   - Verify Google CSE is properly configured
   - Check API quota limits

## 📄 License

This project is licensed under the MIT License.

## 🤝 Contributing

1. Fork the project
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

**Built with ❤️ using Together AI, Google Search, and Gradio**
```

Copy each part separately and combine them in your README.md file!
