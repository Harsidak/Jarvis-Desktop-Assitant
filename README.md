# Jarvis Desktop Assistant

A Python-based AI desktop assistant capable of voice interaction, system command execution, and intelligent conversational abilities using OpenAI or Gemini.

## 🚀 Features
- **Voice Interaction**: 
  - **Speech-to-Text (STT)**: Listens to your commands using Google Speech Recognition.
  - **Text-to-Speech (TTS)**: Responds back to you verbally.
- **LLM Integration**: 
  - Powered by **OpenAI (GPT-3.5)** or **Google Gemini** for intelligent, context-aware responses.
- **System Control**: 
  - Open applications (Notepad, Calculator, Browsers).
  - Check Time and Date.
  - Web Search.

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+ (Python 3.12 recommended)
- A microphone and speakers.

### Steps
1. **Clone/Download** the repository.
2. **Install Dependencies**:
   Open a terminal in the project folder and run:
   ```bash
   pip install -r requirements.txt
   ```
3. **Configuration**:
   - The system creates a `.env` file in `config/.env` on first run (or you can create it manually).
   - Add your API keys:
     ```ini
     LLM_PROVIDER=openai
     OPENAI_API_KEY=sk-...
     # Or for Gemini:
     # LLM_PROVIDER=gemini
     # GEMINI_API_KEY=AIza...
     ```

## 💻 Usage

**Running the Assistant:**
Simply double-click **`run_jarvis.bat`** or run:
```bash
python main.py
```

**Voice Commands:**
- *"What time is it?"*
- *"Open Notepad"*
- *"Search Google for Python tutorials"*
- *"Tell me a joke"* (Handled by LLM)

## 🔧 Troubleshooting
- **Microphone Issues**: Ensure your microphone is the default recording device in Windows Sound settings.
- **API Errors**: If `OPENAI_API_KEY` is missing, LLM features will not work. Check your `.env` file.
- **Audio Dependencies**: If you see `PyAudio` errors, try installing it via `pip install pipwin && pipwin install pyaudio` or ensure C++ build tools are installed.

## 🤝 Contributing
Feel free to add new skills in `core/skills.py`!
