import openai
import google.generativeai as genai
import logging
from config.settings import LLM_PROVIDER, OPENAI_API_KEY, GEMINI_API_KEY, GEMINI_MODEL
from core.memory import ConversationMemory

class LLMClient:
    def __init__(self):
        self.memory = ConversationMemory()
        self.provider = LLM_PROVIDER.lower()
        if self.provider == "openai":
            if not OPENAI_API_KEY:
                logging.warning("OpenAI API Key not found!")
            else:
                openai.api_key = OPENAI_API_KEY
                self.client = openai.Client(api_key=OPENAI_API_KEY)
        elif self.provider == "gemini":
            if not GEMINI_API_KEY:
                logging.warning("Gemini API Key not found!")
            else:
                genai.configure(api_key=GEMINI_API_KEY)
                self.model = genai.GenerativeModel(GEMINI_MODEL)
        
    def get_response(self, prompt):
        """Get response from the configured LLM."""
        try:
            self.memory.add_user_message(prompt)
            
            if self.provider == "openai":
                response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=self.memory.get_messages(),
                    max_tokens=150
                )
                text_response = response.choices[0].message.content.strip()
                self.memory.add_ai_message(text_response)
                return text_response
            
            elif self.provider == "gemini":
                # Basic context for Gemini (simplistic for now)
                # Ideally map history to Gemini's format
                chat = self.model.start_chat(history=[])
                # We are just sending the prompt for now as full history mapping 
                # for Gemini is slightly different (parts/role model vs assistant)
                # To keep it simple, we just send the prompt but ideally we prepend history.
                response = chat.send_message(prompt)
                text_response = response.text
                self.memory.add_ai_message(text_response)
                return text_response
            
            else:
                return "I'm sorry, I don't know how to handle that LLM provider."

        except Exception as e:
            logging.error(f"LLM Error: {e}")
            return "I encountered an error processing your request."
