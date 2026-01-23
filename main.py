import time
import logging
import winsound
from core.voice import VoiceEngine
from core.llm import LLMClient
from core.skills import SkillsRegistry
from config.settings import WAKE_WORD

logging.basicConfig(level=logging.INFO)

def main():
    voice = VoiceEngine()
    llm = LLMClient()
    skills = SkillsRegistry()

    logging.info("Jarvis is starting...")
    voice.speak("System initialized. I am listening.")

    while True:
        try:
            # 1. Listen for audio
            # For simplicity in this v1, we listen continuously or wait for wake word
            
            # Simple interaction loop:
            # User speaks -> Jarvis processes
            
            # winsound.Beep(600, 200) # Optional ding before listening
            user_input = voice.listen()
            
            if not user_input:
                continue

            logging.info(f"User said: {user_input}")
            winsound.Beep(800, 200) # Ding to acknowledge input received

            # Basic Wake Word check (optional if we want to process everything)
            if WAKE_WORD and WAKE_WORD not in user_input:
                # If wake word is set but not present, ignore or maybe process contextually?
                # For v1, let's require the wake word if it's not empty, 
                # OR just process everything if the user is clearly speaking to it.
                # Let's enforce wake word for safety if it's set.
                # But 'listen' might pick up random noise.
                # Let's simple check:
                pass 
            
            # 2. Check for skills
            skill_response = skills.execute_skill(user_input)
            if skill_response:
                logging.info(f"Skill executed: {skill_response}")
                voice.speak(skill_response)
                continue

            # 3. LLM Interaction
            # If no skill matched, ask the LLM
            response = llm.get_response(user_input)
            logging.info(f"LLM Response: {response}")
            voice.speak(response)

        except KeyboardInterrupt:
            logging.info("Stopping...")
            break
        except Exception as e:
            logging.error(f"Error in main loop: {e}")
            voice.speak("I encountered an error.")

if __name__ == "__main__":
    main()
