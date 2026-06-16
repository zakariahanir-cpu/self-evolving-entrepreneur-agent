import os

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return None

def modify_file(file_path, new_content):
    try:
        with open(file_path, 'w') as file:
            file.write(new_content)
    except Exception as e:
        print(f"Error: {e}")

def create_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except Exception as e:
        print(f"Error: {e}")