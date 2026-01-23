import os
import datetime
import subprocess
import webbrowser
import logging

class SkillsRegistry:
    def __init__(self):
        self.skills = {
            "time": self.get_time,
            "date": self.get_date,
            "open": self.open_app,
            "search": self.search_web
        }

    def execute_skill(self, command):
        """
        Parses and executes a skill based on the command.
        This is a simple keyword matcher for now.
        """
        command = command.lower()
        
        if "time" in command:
            return self.get_time()
        elif "date" in command:
            return self.get_date()
        elif "open" in command:
            app = command.replace("open", "").strip()
            return self.open_app(app)
        elif "search" in command or "google" in command:
            query = command.replace("search", "").replace("google", "").replace("for", "").strip()
            return self.search_web(query)
        
        return None

    def get_time(self):
        now = datetime.datetime.now().strftime("%H:%M")
        return f"The current time is {now}"

    def get_date(self):
        today = datetime.date.today().strftime("%B %d, %Y")
        return f"Today's date is {today}"

    def open_app(self, app_name):
        try:
            # Basic common apps mapping
            apps = {
                "notepad": "notepad.exe",
                "calculator": "calc.exe",
                "browser": "start chrome",
                "chrome": "start chrome",
                "edge": "start msedge"
            }
            
            cmd = apps.get(app_name, app_name)
            
            # Using start to launch independently
            os.system(f"start {cmd}") 
            return f"Opening {app_name}"
        except Exception as e:
            logging.error(f"Failed to open {app_name}: {e}")
            return f"I couldn't open {app_name}"

    def search_web(self, query):
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        return f"Searching the web for {query}"
