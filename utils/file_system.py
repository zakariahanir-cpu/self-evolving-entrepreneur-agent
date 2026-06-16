import os

def read_file(path):
    try:
        with open(path, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def write_file(path, content):
    try:
        with open(path, 'w') as file:
            file.write(content)
    except Exception as e:
        print(f"Error writing file: {e}")

def modify_file(path, new_content):
    try:
        with open(path, 'r+') as file:
            file.seek(0)
            file.write(new_content)
            file.truncate()
    except Exception as e:
        print(f"Error modifying file: {e}")