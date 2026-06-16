import os

def read_file(path):
    """Read the contents of a file."""
    try:
        with open(path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return None

def write_file(path, content):
    """Write content to a file."""
    with open(path, 'w') as file:
        file.write(content)

def modify_file(path, content):
    """Modify the contents of a file."""
    try:
        with open(path, 'r+') as file:
            file.seek(0)
            file.write(content)
            file.truncate()
    except FileNotFoundError:
        write_file(path, content)