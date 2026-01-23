import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

# Voice Settings
VOICE_RATE = 175
VOICE_VOLUME = 1.0

# LLM Settings
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openai") # openai, gemini, local
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Application Settings
WAKE_WORD = "jarvis"
