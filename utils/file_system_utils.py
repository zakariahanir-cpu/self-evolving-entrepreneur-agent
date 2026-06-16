import os
import shutil

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def delete_file(path):
    if os.path.exists(path):
        os.remove(path)

def copy_file(source, destination):
    shutil.copy(source, destination)