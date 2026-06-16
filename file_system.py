import os

def read_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: File {file_path} not found."
    except Exception as e:
        return f"Error: {e}"

def write_file(file_path, content):
    try:
        with open(file_path, 'w') as f:
            f.write(content)
        return f"Success: File saved at {file_path}"
    except Exception as e:
        return f"Error: {e}"

def create_file(file_path, content):
    try:
        with open(file_path, 'w') as f:
            f.write(content)
        return f"Success: File created at {file_path}"
    except Exception as e:
        return f"Error: {e}"