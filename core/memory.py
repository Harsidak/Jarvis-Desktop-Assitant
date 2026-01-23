class ConversationMemory:
    def __init__(self, limit=10):
        self.history = []
        self.limit = limit

    def add_user_message(self, message):
        self.history.append({"role": "user", "content": message})
        self._trim()

    def add_ai_message(self, message):
        self.history.append({"role": "assistant", "content": message})
        self._trim()

    def get_messages(self):
        return self.history

    def _trim(self):
        if len(self.history) > self.limit:
            self.history = self.history[-self.limit:]

    def clear(self):
        self.history = []
