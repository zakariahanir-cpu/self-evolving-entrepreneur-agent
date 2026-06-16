import os
import shutil

def create_file(path, content):
    """Create a new file at the specified path with the given content."""
    with open(path, 'w') as f:
        f.write(content)

def modify_file(path, new_content):
    """Modify the content of an existing file at the specified path."""
    with open(path, 'w') as f:
        f.write(new_content)

def delete_file(path):
    """Delete a file at the specified path."""
    os.remove(path)

def read_file(path):
    """Read the content of a file at the specified path."""
    with open(path, 'r') as f:
        return f.read()