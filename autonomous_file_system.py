import os

def create_file(file_path, content):
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
        
    with open(file_path, 'w') as f:
        f.write(content)
    return f"Success: File saved at {file_path}"

# Example usage:
file_path = "example.txt"
content = "This is an example file created by the autonomous agent."
result = create_file(file_path, content)
print(result)