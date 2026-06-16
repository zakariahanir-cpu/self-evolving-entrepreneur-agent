import os

def read_file(path):
    """Read the contents of a file."""
    with open(path, 'r') as file:
        return file.read()

def write_file(path, content):
    """Write content to a file."""
    with open(path, 'w') as file:
        file.write(content)

def modify_file(path, new_content):
    """Modify the contents of a file."""
    with open(path, 'r+') as file:
        file.seek(0)
        file.write(new_content)
        file.truncate()