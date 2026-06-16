import os

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

def write_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except Exception as e:
        print(f"Error writing file: {e}")

def create_file(file_path):
    try:
        open(file_path, 'w').close()
    except Exception as e:
        print(f"Error creating file: {e}")