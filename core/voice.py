import speech_recognition as sr
import pyttsx3
import logging
from config.settings import VOICE_RATE, VOICE_VOLUME

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class VoiceEngine:
    def __init__(self):
        # We will initialize the engine on demand to avoid 'loop already running' errors
        # Initialize STT
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Adjust for ambient noise
        with self.microphone as source:
            logging.info("Adjusting for ambient noise...")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)

    def speak(self, text):
        """Convert text to speech."""
        try:
            logging.info(f"Speaking: {text}")
            # Re-initialize engine every time to prevent event loop blocking issues
            engine = pyttsx3.init()
            engine.setProperty('rate', VOICE_RATE)
            engine.setProperty('volume', VOICE_VOLUME)
            engine.say(text)
            engine.runAndWait()
            # engine.stop() # Ensure it stops
        except Exception as e:
            logging.error(f"TTS Error: {e}")

    def listen(self):
        """Listen for audio input and convert to text."""
        try:
            with self.microphone as source:
                logging.info("Listening...")
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
            
            logging.info("Recognizing...")
            return self.recognizer.recognize_google(audio).lower()
        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            return ""
        except sr.RequestError as e:
            logging.error(f"Could not request results; {e}")
            return ""
        except Exception as e:
            logging.error(f"Error in listen: {e}")
            return ""
