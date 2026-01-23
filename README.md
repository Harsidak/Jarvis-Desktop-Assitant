# Jarvis 2.0 - AI Agent

A fully functional **AI Agent** capable of reasoning, tool usage, and persistent memory.

## 🧠 Capabilities
- **Reasoning Engine**: Uses a ReAct (Reason+Act) loop to solve complex queries.
- **Persistent Memory**: Remembers context across sessions (`brain/memory.json`).
- **Real Web Search**: Can fetch and read search results to answer current events.
- **File System**: Can read and write files on your computer.
- **Media**: Plays YouTube videos and controls system volume.
- **Voice**: Full STT and TTS support.

## 🛠️ Setup
1. **Install**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Configure**:
   - Ensure `.env` has your `GEMINI_API_KEY` (or OpenAI).
   - `GEMINI_MODEL=gemini-1.5-flash` is the default.
3. **Run**:
   ```bash
   .\run_jarvis.bat
   ```

## 🤖 Interaction Examples
- *"Research the history of generic AIs and save the summary to history.txt"*
- *"Play lofi hip hop on YouTube"*
- *"What is on my schedule today?"* (If you add a calendar skill!)
