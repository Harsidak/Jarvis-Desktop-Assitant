import json
import os
import logging

MEMORY_FILE = os.path.join(os.path.dirname(__file__), "../brain/memory.json")

class ConversationMemory:
    def __init__(self, limit=20):
        self.history = []
        self.limit = limit
        self._ensure_brain_dir()
        self.load()

    def _ensure_brain_dir(self):
        directory = os.path.dirname(MEMORY_FILE)
        if not os.path.exists(directory):
            os.makedirs(directory)

    def add_user_message(self, message):
        self.history.append({"role": "user", "content": message})
        self._trim()
        self.save()

    def add_ai_message(self, message):
        self.history.append({"role": "assistant", "content": message})
        self._trim()
        self.save()

    def get_messages(self):
        return self.history

    def _trim(self):
        if len(self.history) > self.limit:
            self.history = self.history[-self.limit:]

    def save(self):
        try:
            with open(MEMORY_FILE, 'w') as f:
                json.dump(self.history, f, indent=2)
        except Exception as e:
            logging.error(f"Failed to save memory: {e}")

    def load(self):
        if os.path.exists(MEMORY_FILE):
            try:
                with open(MEMORY_FILE, 'r') as f:
                    self.history = json.load(f)
            except Exception as e:
                logging.error(f"Failed to load memory: {e}")
                self.history = []

    def clear(self):
        self.history = []
        self.save()
