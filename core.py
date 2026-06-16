import os
import json
from groq import Groq
from duckduckgo_search import DDGS

class SelfEvolvingAgent:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)
        self.memory_path = "memory/long_term_memory.json"
        self.model = "llama-3.3-70b-versatile"
        self.memory = self.load_memory()

    def load_memory(self):
        os.makedirs(os.path.dirname(self.memory_path), exist_ok=True)
        if os.path.exists(self.memory_path):
            with open(self.memory_path, 'r') as f:
                return json.load(f)
        return {"learned_facts": [], "goals": [], "version": 1.2}

    def save_memory(self):
        with open(self.memory_path, 'w') as f:
            json.dump(self.memory, f, indent=4)

    # --- أدوات التعامل مع الملفات الجديدة ---
    def read_file(self, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                return f.read()
        return "Error: File not found."

    def write_file(self, file_path, content):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as f:
            f.write(content)
        return f"Success: File saved at {file_path}"

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
        # إخبار الوكيل بأنه يمتلك أدوات للملفات الآن
        plan_prompt = (f"Current Goal: {goal}\nMemory: {self.memory}\n"
                       "You can now read/write files and search the internet. "
                       "Create a plan. If you need to fix a bug or add a skill, specify the file path and the code.")
        
        plan = self.chat(plan_prompt, system_message="You are the Brain of a self-evolving agent.")
        print(f"Plan: {plan}")

        # 2. Execution (هنا يقرر الوكيل هل يبحث أم يعدل ملفات)
        if "write_file" in plan.lower():
            # منطق بسيط لجعل الوكيل يستخرج الكود ويحفظه (يمكن تطويره لاحقاً)
            print("Agent is attempting to modify/create a file...")
            # هنا يمكن إضافة منطق لاستخراج المسار والكود من 'plan' باستخدام chat ثانية
        
        search_query = self.chat(f"Based on this plan: {plan}, generate 3 simple search keywords.", 
                                 system_message="Generate ONLY keywords.")
        print(f"Searching for: {search_query}")
        search_results = self.search_internet(search_query)

        # 3. Learning & Update Memory
        if "learned_facts" not in self.memory:
            self.memory["learned_facts"] = []
        
        self.memory["learned_facts"].append({"query": search_query, "info": "Processed cycle"})
        self.save_memory()
        print("Cycle completed.")

if __name__ == "__main__":
    API_KEY = os.getenv("GROQ_API_KEY")
    if API_KEY:
        agent = SelfEvolvingAgent(API_KEY)
        agent.run_cycle()
        
