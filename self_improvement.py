import os
from groq import Groq

class SelfImprovement:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)
        self.model = "llama-3.3-70b-versatile"

    def analyze_and_improve(self, file_path):
        with open(file_path, 'r') as f:
            code = f.read()
        
        prompt = f"""
        Here is my current Python code:
        ---
        {code}
        ---
        As an expert AI engineer, suggest one improvement or a new feature to add to this code to make it more 'autonomous' or 'intelligent'. 
        Provide ONLY the full updated code. Do not explain.
        """
        
        response = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=self.model,
        )
        
        new_code = response.choices[0].message.content
        # Clean up code blocks if present
        if "```python" in new_code:
            new_code = new_code.split("```python")[1].split("```")[0]
        elif "```" in new_code:
            new_code = new_code.split("```")[1].split("```")[0]
            
        with open(file_path, 'w') as f:
            f.write(new_code.strip())
        print(f"Improved {file_path} successfully.")

if __name__ == "__main__":
    API_KEY = os.getenv("GROQ_API_KEY")
    if API_KEY:
        improver = SelfImprovement(API_KEY)
        improver.analyze_and_improve("self_evolving_agent/core.py")
