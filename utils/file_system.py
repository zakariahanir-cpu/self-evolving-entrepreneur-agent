import os
import shutil

def create_directory(path):
    """Create a directory at the specified path."""
    try:
        os.makedirs(path, exist_ok=True)
    except OSError as e:
        print(f"Error creating directory: {e}")

def delete_file(path):
    """Delete a file at the specified path."""
    try:
        os.remove(path)
    except OSError as e:
        print(f"Error deleting file: {e}")

def copy_file(src, dest):
    """Copy a file from the source path to the destination path."""
    try:
        shutil.copy2(src, dest)
    except OSError as e:
        print(f"Error copying file: {e}")