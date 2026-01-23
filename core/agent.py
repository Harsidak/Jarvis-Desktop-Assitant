import json
import logging
from core.llm import LLMClient
from core.skills import SkillsRegistry
from core.memory import ConversationMemory

class Agent:
    def __init__(self):
        self.llm = LLMClient()
        self.skills = SkillsRegistry()
        self.memory = self.llm.memory # Share memory instance

    def run(self, user_input):
        """
        The main Agent Loop (Reasoning Engine).
        Decides whether to answer directly or use a tool.
        """
        # 1. Update Memory
        # (This happens inside llm.get_response currently, but we might want to decouple it
        #  so "thoughts" aren't saved as user/assistant pairs, but we'll keep it simple for now)
        
        # 2. Logic:
        # We need a system prompt that tells the LLM it has tools.
        system_prompt = self._build_system_prompt()
        
        # Construct the full prompt including history
        # For simplicity in this non-LangChain implementation, we append the system instructions
        # to the latest user message or inject it as a system message if provider supports it.
        # Our LLMClient wrapper is simple, so we'll prepend to the user prompt for the decision step.
        
        full_prompt = f"""{system_prompt}

USER INPUT: {user_input}

Think step-by-step.
If you need to use a tool, output a JSON object: {{"tool": "tool_name", "args": "arguments"}}
If you have the answer, output: FINAL ANSWER: [your response]
"""
        
        # 3. Get LLM Decision
        response = self.llm.get_response(full_prompt) # This saves to memory, which is okay-ish but redundant prompts might clutter history.
        
        logging.info(f"Agent Thought: {response}")

        # 4. Check for Tool Call
        if '{"tool":' in response:
            try:
                # Naive parsing. Ideally use a JSON parser on the substring.
                start = response.find('{')
                end = response.rfind('}') + 1
                json_str = response[start:end]
                tool_data = json.loads(json_str)
                
                tool_name = tool_data.get("tool")
                tool_args = tool_data.get("args")
                
                logging.info(f"Agent Invoking Tool: {tool_name} with {tool_args}")
                
                # Execute Tool
                if tool_name in self.skills.skills:
                    tool_func = self.skills.skills[tool_name]
                    # We need to handle args. simpler if we pass the string or unpack
                    # Our skills currently take 1 arg usually (command or query)
                    tool_result = tool_func(tool_args)
                else:
                    tool_result = f"Error: Tool {tool_name} not found."
                    
                # 5. Observation (Feed back to LLM)
                observation_prompt = f"OBSERVATION: {tool_result}\nNow provide the FINAL ANSWER based on this."
                final_response = self.llm.get_response(observation_prompt)
                return final_response
                
            except Exception as e:
                logging.error(f"Agent Tool Error: {e}")
                return f"I tried to use a tool but failed: {e}"

        # If no tool called (or only Final Answer found)
        if "FINAL ANSWER:" in response:
            return response.split("FINAL ANSWER:")[-1].strip()
            
        return response

    def _build_system_prompt(self):
        return """You are Jarvis, an advanced AI Assistant.
You have access to the following tools:
- google_search(query): Get proper search results text.
- play(song): Play music on YouTube.
- open(app_name): Open a desktop application or website.
- write_file(filename, content): Save text to a file.
- read_file(filename): Read a file.
- time(): Get current time.
- date(): Get current date.

When asked a question, analyze if you need external info.
If yes, CALL A TOOL.
If no, answer directly.
"""
