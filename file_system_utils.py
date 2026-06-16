import pathlib

def read_file(file_path):
    """Read the contents of a file."""
    file = pathlib.Path(file_path)
    return file.read_text()

def write_file(file_path, content):
    """Write content to a file."""
    file = pathlib.Path(file_path)
    file.write_text(content)

def create_file(file_path, content):
    """Create a new file with the given content."""
    file = pathlib.Path(file_path)
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(content)