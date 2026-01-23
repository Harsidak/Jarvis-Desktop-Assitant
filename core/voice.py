import speech_recognition as sr
import pyttsx3
import logging
from config.settings import VOICE_RATE, VOICE_VOLUME

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class VoiceEngine:
    def __init__(self):
        # Initialize TTS
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', VOICE_RATE)
        self.engine.setProperty('volume', VOICE_VOLUME)
        
        # Initialize STT
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Adjust for ambient noise
        with self.microphone as source:
            logging.info("Adjusting for ambient noise...")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)

    def speak(self, text):
        """Convert text to speech."""
        logging.info(f"Speaking: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

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
