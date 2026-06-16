import os

class FileSystemInterface:
    def __init__(self, root_dir):
        self.root_dir = root_dir

    def read_file(self, filename):
        file_path = os.path.join(self.root_dir, filename)
        with open(file_path, 'r') as file:
            return file.read()

    def write_file(self, filename, content):
        file_path = os.path.join(self.root_dir, filename)
        with open(file_path, 'w') as file:
            file.write(content)

    def create_file(self, filename):
        file_path = os.path.join(self.root_dir, filename)
        with open(file_path, 'w') as file:
            pass

    def delete_file(self, filename):
        file_path = os.path.join(self.root_dir, filename)
        os.remove(file_path)