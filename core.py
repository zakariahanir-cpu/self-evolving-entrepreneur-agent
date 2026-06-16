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
        # إضافة الذاكرة قصيرة المدى لمنع التكرار (تخزن آخر 5 أحداث)
        self.short_term_memory = deque(maxlen=5)

    def load_memory(self):
        """تحميل الذاكرة مع حماية ضد الأخطاء"""
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
            "version": 1.2
        }

    def save_memory(self):
        """حفظ حالة الوكيل"""
        with open(self.memory_path, 'w') as f:
            json.dump(self.memory, f, indent=4)

    def read_file(self, file_path):
        """قراءة الملفات لتمكين الوكيل من فهم كوده الحالي"""
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                return f.read()
        return f"Error: File {file_path} not found."

    def write_file(self, file_path, content):
        """إنشاء وتعديل الملفات"""
        directory = os.path.dirname(file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
            
        with open(file_path, 'w') as f:
            f.write(content)
        return f"Success: File saved at {file_path}"

    def chat(self, prompt, system_message="You are a self-evolving AI agent."):
        """التواصل مع العقل المدبر (LLM)"""
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
        """البحث في الإنترنت"""
        try:
            with DDGS() as ddgs:
                results = [r for r in ddgs.text(query, max_results=5)]
                return results if results else "No results found."
        except Exception as e:
            return f"Search error: {e}"

    def run_cycle(self):
        print("--- [AGENT CYCLE START] ---")
        
        # 1. التخطيط والتحليل
        goal = self.memory["goals"][0]
        current_code = self.read_file(__file__)

        # تجهيز سياق الذاكرة قصيرة المدى للموجه (Prompt)
        short_term_context = "\nRecent Actions (Short-Term Memory):\n" + "\n".join(self.short_term_memory) if self.short_term_memory else ""

        # استخدام علامات اقتباس ثلاثية لتجنب أي تداخل مع علامات الاقتباس الداخلية
        plan_prompt = f"""
Current Goal: {goal}
Memory Facts: {self.memory['learned_facts'][-2:] if self.memory['learned_facts'] else 'None'}
Current Code Context: {current_code}
{short_term_context}

Instructions:
1. Analyze your current state and create a technical plan.
2. To create/update a file, use EXACTLY this format:
FILE: path/to/filename.py
```python
# code
```
3. Focus on creating tools that help you achieve your goal autonomously.
"""
        
        plan = self.chat(plan_prompt, system_message="You are an autonomous AI Engineer.")
        print(f"PLAN:\n{plan}\n")
        self.short_term_memory.append(f"Generated Plan: {plan[:100]}...")

        # 2. التنفيذ البرمجي
        file_matches = re.findall(r"FILE:\s*(.*?)\s*```python\n(.*?)\n```", plan, re.DOTALL)
        
        for file_path, code in file_matches:
            file_path = file_path.strip()
            if file_path:
                print(f"ACTION: Writing to {file_path}...")
                result = self.write_file(file_path, code.strip())
                print(result)
                self.short_term_memory.append(f"Wrote to file: {file_path}")

        # 3. البحث
        search_query = self.chat(
            f"Based on your plan: {plan}, what are 3 simple keywords to learn more?", 
            system_message="Output ONLY 3 keywords separated by spaces."
        )
        print(f"SEARCHING: {search_query}")
        search_results = self.search_internet(search_query)
        self.short_term_memory.append(f"Searched for: {search_query}")

        # 4. التحديث والتعلم
        learn_prompt = f"Results: {search_results}\nSummarize key technical insights for your memory."
        learning = self.chat(learn_prompt)
        
        self.memory["learned_facts"].append({
            "goal": goal,
            "learned": learning
        })
        
        self.save_memory()
        self.short_term_memory.append(f"Learned: {learning[:100]}...")
        print("--- [AGENT CYCLE COMPLETE] ---")


if __name__ == "__main__":
    API_KEY = os.getenv("GROQ_API_KEY")
    if API_KEY:
        agent = SelfEvolvingAgent(API_KEY)
        agent.run_cycle()
    else:
        print("FATAL: GROQ_API_KEY not found.")
        
