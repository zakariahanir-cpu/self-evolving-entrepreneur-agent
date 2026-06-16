import os
import json
import re
from collections import deque
from groq import Groq
try:
    from duckduckgo_search import DDGS
except ImportError:
    from ddgs import DDGS
from sklearn.feature_extraction import text
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

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
        try:
            with DDGS() as ddgs:
                results = list(ddgs.text(query, max_results=5))
                return results if results else "No results found."
        except Exception as e:
            print(f"Search Warning: {e}")
            return f"Search error: {e}"

    def web_scrape(self, url):
        # Implement web scraping using BeautifulSoup and requests
        import requests
        from bs4 import BeautifulSoup
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.find_all('a')

    def analyze_data(self, data):
        # Implement machine learning analysis using scikit-learn
        vectorizer = text.TfidfVectorizer()
        X = vectorizer.fit_transform(data)
        y = [1 if 'vulnerability' in text else 0 for text in data]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        clf = RandomForestClassifier()
        clf.fit(X_train, y_train)
        return clf.predict(X_test)

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