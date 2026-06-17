import os
import shutil

def create_directory(path):
    """Create a new directory at the specified path."""
    try:
        os.makedirs(path, exist_ok=True)
        return f"Directory created at {path}"
    except Exception as e:
        return f"Error creating directory: {e}"

def delete_file(path):
    """Delete a file at the specified path."""
    try:
        os.remove(path)
        return f"File deleted at {path}"
    except Exception as e:
        return f"Error deleting file: {e}"

def modify_file(path, content):
    """Modify the contents of a file at the specified path."""
    try:
        with open(path, 'w') as f:
            f.write(content)
        return f"File modified at {path}"
    except Exception as e:
        return f"Error modifying file: {e}"