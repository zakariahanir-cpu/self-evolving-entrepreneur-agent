import os

def read_file(path):
    """Read the contents of a file."""
    try:
        with open(path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None

def write_file(path, content):
    """Write content to a file."""
    try:
        with open(path, 'w') as file:
            file.write(content)
    except Exception as e:
        print(f"Error writing to file: {path} - {str(e)}")

def create_directory(path):
    """Create a new directory."""
    try:
        os.mkdir(path)
    except Exception as e:
        print(f"Error creating directory: {path} - {str(e)}")