import os
import json
from security_environment import SecurityEnvironment

class SelfEvolvingAgent:
    def __init__(self, api_key):
        # ...
        self.security_environment = SecurityEnvironment()

    def run_cycle(self):
        # ...
        goal = self.memory["goals"][0]
        current_code = self.read_file(__file__)
        short_term_context = "\nRecent Actions:\n" + "\n".join(self.short_term_memory) if self.short_term_memory else ""

        plan_prompt = f"""
Current Goal: {goal}
Memory Facts: {self.memory['learned_facts'][-2:] if self.memory['learned_facts'] else 'None'}
Current Code Context: {current_code}
{short_term_context}

Instructions:
1. Create a technical plan to improve yourself.
2. Format for files:
FILE: path/to/filename.py