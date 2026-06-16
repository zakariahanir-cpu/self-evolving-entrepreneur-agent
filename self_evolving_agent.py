# Enhanced read_file method to handle different file types
def read_file(self, file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            if file_path.endswith('.py'):
                return f.read()
            elif file_path.endswith('.json'):
                return json.load(f)
            else:
                return f"Error: Unsupported file type {file_path}"
    return f"Error: File {file_path} not found."

# Enhanced write_file method to handle different file types
def write_file(self, file_path, content):
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
    with open(file_path, 'w') as f:
        if file_path.endswith('.py'):
            f.write(content)
        elif file_path.endswith('.json'):
            json.dump(content, f, indent=4)
        else:
            return f"Error: Unsupported file type {file_path}"
    return f"Success: File saved at {file_path}"

# New method to generate code snippets
def generate_code(self, prompt):
    response = self.chat(prompt, system_message="You are an autonomous AI Engineer.")
    return response

# New method to integrate search results into the knowledge base
def update_memory(self, search_results):
    self.memory["learned_facts"].append(f"Search results: {str(search_results)[:200]}")
    self.save_memory()