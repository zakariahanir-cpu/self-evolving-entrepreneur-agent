from utils.file_system import create_directory, delete_file, copy_file
from utils.autonomous_scripting import run_script

class SelfEvolvingAgent:
    # ...

    def run_cycle(self):
        # ...
        plan_prompt = f"""
Current Goal: {goal}
Memory Facts: {self.memory['learned_facts'][-2:] if self.memory['learned_facts'] else 'None'}
Current Code Context: {current_code}
{short_term_context}

Instructions:
1. Create a technical plan to improve yourself.
2. Format for files:
FILE: path/to/filename.py