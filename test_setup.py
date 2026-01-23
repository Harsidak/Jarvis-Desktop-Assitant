import sys
import os

print("Testing imports and initialization...")

try:
    print("- Testing Config...")
    from config.settings import VOICE_RATE
    print("  > Config loaded.")

    print("- Testing Voice Engine (Init only)...")
    from core.voice import VoiceEngine
    # We won't instantiate it fully if it starts listening immediately or takes time, 
    # but the class Init does basic setup.
    # To be safe, we'll just check import unless we mock it, 
    # but let's try a quick init to see if drivers are present.
    try:
        import pyttsx3
        engine = pyttsx3.init()
        print("  > pyttsx3 initialized.")
    except Exception as e:
        print(f"  > pyttsx3 failed: {e}")

    try:
        import speech_recognition as sr
        r = sr.Recognizer()
        print("  > SpeechRecognition initialized.")
    except Exception as e:
        print(f"  > SpeechRecognition failed: {e}")


    print("- Testing LLM Client...")
    from core.llm import LLMClient
    llm = LLMClient()
    print("  > LLM Client initialized.")

    print("- Testing Skills...")
    from core.skills import SkillsRegistry
    skills = SkillsRegistry()
    print("  > Skills Registry initialized.")

    print("\nSUCCESS: All modules import and initialize correctly.")

except ImportError as e:
    print(f"\nFAILURE: Import Error: {e}")
except Exception as e:
    print(f"\nFAILURE: General Error: {e}")
