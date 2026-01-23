import openai
import google.generativeai as genai
import logging
from config.settings import LLM_PROVIDER, OPENAI_API_KEY, GEMINI_API_KEY

class LLMClient:
    def __init__(self):
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
                self.model = genai.GenerativeModel('gemini-pro')
        
    def get_response(self, prompt):
        """Get response from the configured LLM."""
        try:
            if self.provider == "openai":
                response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo", # Default to 3.5 for speed/cost
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=150
                )
                return response.choices[0].message.content.strip()
            
            elif self.provider == "gemini":
                response = self.model.generate_content(prompt)
                return response.text
            
            else:
                return "I'm sorry, I don't know how to handle that LLM provider."

        except Exception as e:
            logging.error(f"LLM Error: {e}")
            return "I encountered an error processing your request."
