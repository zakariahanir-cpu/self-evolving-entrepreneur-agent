import os

def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def write_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)

def create_directory(dir_path):
    os.makedirs(dir_path, exist_ok=True)

def delete_directory(dir_path):
    import shutil
    shutil.rmtree(dir_path)

def get_file_listing(dir_path):
    return os.listdir(dir_path)