import os
import json
import re
from collections import deque
from groq import Groq
from duckduckgo_search import DDGS

class SelfEvolvingAgent:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)
        self.memory_path = "memory/long_term_memory.json"
        self.model = "llama-3.3-70b-versatile"
        self.memory = self.load_memory()
        self.short_term_memory = deque(maxlen=5)

    def load_memory(self):
        os.makedirs(os.path.dirname(self.memory_path), exist_ok=True)
        if os.path.exists(self.memory_path):
            try:
                with open(self.memory_path, 'r') as f:
                    data = json.load(f)
                    if "learned_facts" not in data: data["learned_facts"] = []
                    if "goals" not in data: data["goals"] = ["Autonomous evolution and security research"]
                    return data
            except:
                pass
        return {
            "learned_facts": [], 
            "goals": ["Enable autonomous file system operations and self-evolution"], 
            "version": 1.3
        }

    def save_memory(self):
        with open(self.memory_path, 'w') as f:
            json.dump(self.memory, f, indent=4)

    def read_file(self, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                return f.read()
        return f"Error: File {file_path} not found."

    def write_file(self, file_path, content):
        directory = os.path.dirname(file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
        with open(file_path, 'w') as f:
            f.write(content)
        return f"Success: File saved at {file_path}"

    def chat(self, prompt, system_message="You are a self-evolving AI agent."):
        try:
            response = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": prompt}
                ],
                model=self.model,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Chat Error: {e}"

    def search_internet(self, query):
        """تحديث دالة البحث لتتوافق مع الإصدار الجديد من DDGS"""
        try:
            with DDGS() as ddgs:
                # تحويل النتائج إلى قائمة فوراً لضمان الحصول على البيانات
                results = list(ddgs.text(query, max_results=5))
                return results if results else "No results found."
        except Exception as e:
            print(f"Search Warning: {e}")
            return f"Search error: {e}"

    def run_cycle(self):
        print("--- [AGENT CYCLE START] ---")
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
```python
# code
```
"""
        plan = self.chat(plan_prompt, system_message="You are an autonomous AI Engineer.")
        print(f"PLAN:\n{plan}\n")
        
        # تنفيذ التعديلات المقترحة
        file_matches = re.findall(r"FILE:\s*(.*?)\s*```python\n(.*?)\n```", plan, re.DOTALL)
        for file_path, code in file_matches:
            print(f"ACTION: Updating {file_path.strip()}...")
            self.write_file(file_path.strip(), code.strip())

        # عملية البحث والتعلم
        search_query = self.chat(f"Search keywords for: {goal}", system_message="Output ONLY 3 keywords.")
        print(f"SEARCHING: {search_query}")
        search_results = self.search_internet(search_query)
        
        # حفظ ما تم تعلمه
        self.memory["learned_facts"].append(f"Search results for {search_query}: {str(search_results)[:200]}")
        self.save_memory()
        print("--- [AGENT CYCLE END] ---")

if __name__ == "__main__":
    api_key = os.getenv("GROQ_API_KEY")
    if api_key:
        agent = SelfEvolvingAgent(api_key)
        agent.run_cycle()
    else:
        print("Error: GROQ_API_KEY not found.")
        
