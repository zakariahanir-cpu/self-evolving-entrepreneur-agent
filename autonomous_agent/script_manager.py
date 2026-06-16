import importlib.util
import os

def load_script(path):
    """Load a Python script from the specified path."""
    spec = importlib.util.spec_from_file_location("script", path)
    script = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(script)
    return script

def create_script(path, content):
    """Create a new Python script at the specified path with the given content."""
    with open(path, 'w') as f:
        f.write(content)

def modify_script(path, new_content):
    """Modify the content of an existing Python script at the specified path."""
    with open(path, 'w') as f:
        f.write(new_content)