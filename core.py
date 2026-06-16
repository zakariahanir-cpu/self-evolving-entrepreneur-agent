import os
import json
import re
from groq import Groq
from duckduckgo_search import DDGS

class SelfEvolvingAgent:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)
        self.memory_path = "memory/long_term_memory.json"
        self.model = "llama-3.3-70b-versatile"
        self.memory = self.load_memory()

    def load_memory(self):
        """تحميل الذاكرة والتأكد من وجود المجلدات والحقول الأساسية"""
        os.makedirs(os.path.dirname(self.memory_path), exist_ok=True)
        if os.path.exists(self.memory_path):
            with open(self.memory_path, 'r') as f:
                data = json.load(f)
                # التأكد من وجود الحقول الأساسية لتجنب KeyError
                if "learned_facts" not in data: data["learned_facts"] = []
                if "goals" not in data: data["goals"] = ["Evolve and expand capabilities"]
                return data
        return {
            "learned_facts": [], 
            "goals": ["Autonomous file system operations and self-evolution"], 
            "version": 1.2
        }

    def save_memory(self):
        """حفظ الحالة الحالية للذاكرة"""
        with open(self.memory_path, 'w') as f:
            json.dump(self.memory, f, indent=4)

    def read_file(self, file_path):
        """قراءة محتوى أي ملف في المستودع"""
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                return f.read()
        return f"Error: File {file_path} not found."

    def write_file(self, file_path, content):
        """إنشاء أو تعديل ملف مع إنشاء المجلدات اللازمة تلقائياً"""
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as f:
            f.write(content)
        return f"Success: File saved at {file_path}"

    def chat(self, prompt, system_message="You are a self-evolving AI agent."):
        """التواصل مع نموذج اللغة (LLM)"""
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
        """البحث في الإنترنت باستخدام كلمات مفتاحية بسيطة"""
        try:
            with DDGS() as ddgs:
                results = [r for r in ddgs.text(query, max_results=5)]
                return results
        except Exception as e:
            return f"Search error: {e}"

    def run_cycle(self):
        print("--- Starting Execution Cycle ---")
        
        # 1. التخطيط (Planning)
        goal = self.memory["goals"][0]
        plan_prompt = (
            f"Current Goal: {goal}\n"
            f"Current Memory: {self.memory}\n\n"
            "Instructions:\n"
            "1. Create a plan to achieve the goal.\n"
            "2. If you need to create/update a file, use this format:\n"
            "FILE: path/to/filename.py\n"
            "```python\n# your code here\n```\n"
            "3. You can read any file to understand your own code before modifying it."
        )
        
        plan = self.chat(plan_prompt, system_message="You are the Architect of a self-evolving system.")
        print(f"Plan Generated:\n{plan}\n")

        # 2. التنفيذ (Execution - File Operations)
        # البحث عن أنماط إنشاء الملفات في رد الوكيل
        file_matches = re.findall(r"FILE:\s*(.*?)\s*```python\n(.*?)\n```", plan, re.DOTALL)
        
        for file_path, code in file_matches:
            print(f"Agent Action: Writing code to {file_path}...")
            result = self.write_file(file_path.strip(), code.strip())
            print(result)

        # 3. البحث والتعلم (Search & Learning)
        search_query = self.chat(
            f"Based on this plan: {plan}, generate 3 simple keywords for a search engine.", 
            system_message="Generate ONLY 3-4 keywords, no quotes, no sentences."
        )
        print(f"Searching for: {search_query}")
        search_results = self.search_internet(search_query)

        # 4. تحديث الذاكرة (Memory Update)
        learn_prompt = f"Search Results: {search_results}\nSummarize what was learned and how it helps the goal."
        learning = self.chat(learn_prompt)
        
        self.memory["learned_facts"].append({
            "cycle_goal": goal,
            "search_query": search_query,
            "result_summary": learning
        })
        
        self.save_memory()
        print("--- Cycle Completed Successfully ---")

if __name__ == "__main__":
    API_KEY = os.getenv("GROQ_API_KEY")
    if API_KEY:
        agent = SelfEvolvingAgent(API_KEY)
        agent.run_cycle()
    else:
        print("Error: GROQ_API_KEY environment variable not found.")
        
