import os

class FileSystemInterface:
    def __init__(self, root_dir):
        self.root_dir = root_dir

    def read_file(self, file_path):
        try:
            with open(os.path.join(self.root_dir, file_path), 'r') as file:
                return file.read()
        except FileNotFoundError:
            return None

    def write_file(self, file_path, content):
        try:
            with open(os.path.join(self.root_dir, file_path), 'w') as file:
                file.write(content)
        except Exception as e:
            print(f"Error writing file: {e}")

    def create_file(self, file_path, content):
        try:
            with open(os.path.join(self.root_dir, file_path), 'x') as file:
                file.write(content)
        except FileExistsError:
            print(f"File already exists: {file_path}")
        except Exception as e:
            print(f"Error creating file: {e}")