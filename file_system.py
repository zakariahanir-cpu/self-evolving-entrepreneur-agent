import os

def read_file(path):
    """Read the contents of a file."""
    with open(path, 'r') as file:
        return file.read()

def write_file(path, contents):
    """Write contents to a file."""
    with open(path, 'w') as file:
        file.write(contents)

def modify_file(path, modifier):
    """Modify the contents of a file using a modifier function."""
    contents = read_file(path)
    modified_contents = modifier(contents)
    write_file(path, modified_contents)