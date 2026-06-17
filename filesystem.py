import os

class FileSystem:
    def __init__(self):
        pass

    def read_file(self, file_path):
        with open(file_path, "r") as f:
            return f.read()

    def write_file(self, file_path, content):
        with open(file_path, "w") as f:
            f.write(content)