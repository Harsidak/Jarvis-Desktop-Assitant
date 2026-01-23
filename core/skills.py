import os
import datetime
import subprocess
import webbrowser
import logging
import pywhatkit
import pyautogui
from googlesearch import search as google_search

class SkillsRegistry:
    def __init__(self):
        self.skills = {
            "time": self.get_time,
            "date": self.get_date,
            "open": self.open_app,
            "search": self.search_web,
            "play": self.play_youtube,
            "volume": self.control_volume,
            "write_file": self.write_file,
            "read_file": self.read_file,
            "google_search": self.get_search_results
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
        elif "play" in command:
            # "play despacito on youtube" -> "despacito on youtube" -> "despacito"
            song = command.replace("play", "").replace("on youtube", "").strip()
            return self.play_youtube(song)
        elif "volume" in command or "mute" in command or "unmute" in command:
            return self.control_volume(command)
        
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
                "edge": "start msedge",
                "command prompt": "cmd.exe",
                "cmd": "cmd.exe"
            }
            
            # Websites to open in browser instead of as apps
            websites = {
                "youtube": "https://www.youtube.com",
                "google": "https://www.google.com",
                "facebook": "https://www.facebook.com",
                "twitter": "https://www.x.com",
                "instagram": "https://www.instagram.com",
                "reddit": "https://www.reddit.com",
                "linkedin": "https://www.linkedin.com"
            }

            if app_name in websites:
                url = websites[app_name]
                # Force open in Chrome
                subprocess.Popen(["start", "chrome", url], shell=True)
                return f"Opening {app_name} in Chrome"
            
            cmd = apps.get(app_name, app_name)
            
            # Using start to launch independently
            os.system(f"start {cmd}") 
            return f"Opening {app_name}"
        except Exception as e:
            logging.error(f"Failed to open {app_name}: {e}")
            return f"I couldn't open {app_name}"

    def search_web(self, query):
        url = f"https://www.google.com/search?q={query}"
        try:
            # Try to start chrome explicitly
            subprocess.Popen(["start", "chrome", url], shell=True)
            return f"Searching the web for {query}"
        except:
             # Fallback
            webbrowser.open(url)
            return f"Searching the web for {query}"

    def play_youtube(self, song):
        try:
            pywhatkit.playonyt(song)
            return f"Playing {song} on YouTube"
        except Exception as e:
            logging.error(f"YouTube Error: {e}")
            return "I couldn't play that video."

    def control_volume(self, command):
        try:
            if "up" in command or "increase" in command:
                pyautogui.press("volumeup", presses=5)
                return "Volume increased"
            elif "down" in command or "decrease" in command:
                pyautogui.press("volumedown", presses=5)
                return "Volume decreased"
            elif "mute" in command:
                pyautogui.press("volumemute")
                return "Volume muted"
            elif "unmute" in command:
                pyautogui.press("volumemute") # Toggle
                return "Volume unmuted"
            return "Volume command not recognized"
        except Exception as e:
            logging.error(f"Volume Error: {e}")
    def write_file(self, filename, content):
        try:
            with open(filename, 'w') as f:
                f.write(content)
            return f"Successfully wrote to {filename}"
        except Exception as e:
            return f"Error writing file: {e}"

    def read_file(self, filename):
        try:
            if not os.path.exists(filename):
                return "File not found."
            with open(filename, 'r') as f:
                return f.read()
        except Exception as e:
            return f"Error reading file: {e}"

    def get_search_results(self, query, num_results=3):
        try:
            results = []
            for j in google_search(query, num=num_results, stop=num_results, pause=2):
                results.append(j)
            return f"Search Results for '{query}':\n" + "\n".join(results)
        except Exception as e:
            return f"Search Error: {e}"
