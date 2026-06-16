import os
import shutil

def create_directory(path):
    os.makedirs(path, exist_ok=True)

def delete_file(path):
    os.remove(path)

def copy_file(src, dst):
    shutil.copy(src, dst)