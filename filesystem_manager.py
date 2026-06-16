import os
import shutil

class FileSystemManager:
    def create_file(self, file_path):
        # Create a new file
        with open(file_path, 'w') as f:
            pass

    def delete_file(self, file_path):
        # Delete a file
        os.remove(file_path)

    def rename_file(self, old_file_path, new_file_path):
        # Rename a file
        os.rename(old_file_path, new_file_path)

    def create_directory(self, dir_path):
        # Create a new directory
        os.makedirs(dir_path, exist_ok=True)

    def delete_directory(self, dir_path):
        # Delete a directory
        shutil.rmtree(dir_path)

    def check_file_existence(self, file_path):
        # Check if a file exists
        return os.path.exists(file_path)

    def check_file_permissions(self, file_path):
        # Check file permissions
        return os.access(file_path, os.R_OK)