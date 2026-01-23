import time
import logging
import winsound
from core.voice import VoiceEngine
from core.agent import Agent
from config.settings import WAKE_WORD

logging.basicConfig(level=logging.INFO)

def main():
    agent = Agent()
    voice = VoiceEngine()

    logging.info("Jarvis is starting...")
    voice.speak("System initialized. I am listening.")

    while True:
        try:
            # 1. Listen for audio
            # winsound.Beep(600, 200) # Optional ding before listening
            user_input = voice.listen()
            
            if not user_input:
                continue

            logging.info(f"User said: {user_input}")
            winsound.Beep(800, 200) # Ding to acknowledge input received

            # Basic Wake Word check
            if WAKE_WORD and WAKE_WORD not in user_input:
               pass

            # 2. Agent Logic (ReAct Loop)
            # The agent decides whether to use a skill or answer directly.
            response = agent.run(user_input)
            
            logging.info(f"Agent Response: {response}")
            voice.speak(response)

        except KeyboardInterrupt:
            logging.info("Stopping...")
            break
        except Exception as e:
            logging.error(f"Error in main loop: {e}")
            voice.speak("I encountered an error.")

if __name__ == "__main__":
    main()
