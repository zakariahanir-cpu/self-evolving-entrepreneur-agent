import os

def list_directories():
    return os.listdir()

def create_directory(dir_name):
    os.mkdir(dir_name)

def change_directory(dir_name):
    os.chdir(dir_name)