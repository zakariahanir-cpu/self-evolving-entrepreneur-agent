import os

def read_file(path):
    with open(path, 'r') as file:
        return file.read()

def write_file(path, content):
    with open(path, 'w') as file:
        file.write(content)

def create_file(path):
    open(path, 'w').close()

def modify_file(path, new_content):
    with open(path, 'w') as file:
        file.write(new_content)