import os
import json
from groq import Groq
from duckduckgo_search import DDGS

class SelfEvolvingAgent:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)
        self.memory_path = "memory/long_term_memory.json"
        self.skills_path = "skills/"
        self.model = "llama-3.3-70b-versatile"
        self.memory = self.load_memory()

    def load_memory(self):
        if os.path.exists(self.memory_path):
            with open(self.memory_path, 'r') as f:
                return json.load(f)
        return {"learned_facts": [], "goals": ["Become a digital entrepreneur", "Operate under a digital pseudonym"], "version": 1.1}

    def save_memory(self):
        with open(self.memory_path, 'w') as f:
            json.dump(self.memory, f, indent=4)

    def chat(self, prompt, system_message="You are a self-evolving AI agent."):
        response = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ],
            model=self.model,
            temperature=0.7
        )
        return response.choices[0].message.content

    def search_internet(self, query):
        with DDGS() as ddgs:
            results = [r for r in ddgs.text(query, max_results=5)]
            return results

    def run_cycle(self):
        print("Starting execution cycle...")
        
        # 1. Planning
        goal = self.memory["goals"][0]
        plan_prompt = f"Current Goal: {goal}\nMemory: {self.memory}\nCreate a step-by-step plan to achieve this goal using internet search."
        plan = self.chat(plan_prompt, system_message="You are the Brain of a self-evolving agent. Plan your next move.")
        print(f"Plan: {plan}")

        # 2. Execution (Search)
        search_query = self.chat(f"Based on this plan: {plan}, what is the best search query to learn something new?", system_message="Generate only the search query.")
        print(f"Searching for: {search_query}")
        search_results = self.search_internet(search_query)

        # 3. Learning & Reflection
        learn_prompt = f"Search Results: {search_results}\nWhat did you learn from this? Summarize key facts and how you can improve yourself."
        learning = self.chat(learn_prompt)
        print(f"Learned: {learning}")

        # 4. Update Memory
        self.memory["learned_facts"].append({"query": search_query, "info": learning})
        self.save_memory()
        print("Cycle completed and memory updated.")

if __name__ == "__main__":
    # Note: API key should be provided via environment variable
    API_KEY = os.getenv("GROQ_API_KEY")
    if API_KEY:
        agent = SelfEvolvingAgent(API_KEY)
        agent.run_cycle()
    else:
        print("GROQ_API_KEY not found.")
