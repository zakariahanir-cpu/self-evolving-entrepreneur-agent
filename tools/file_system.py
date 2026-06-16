import os
import pathlib

class FileSystem:
    def __init__(self):
        self.root_dir = pathlib.Path(__file__).parent

    def read_file(self, file_path):
        with open(file_path, 'r') as file:
            return file.read()

    def write_file(self, file_path, content):
        with open(file_path, 'w') as file:
            file.write(content)

    def modify_file(self, file_path, new_content):
        with open(file_path, 'r+') as file:
            file.seek(0)
            file.write(new_content)
            file.truncate()