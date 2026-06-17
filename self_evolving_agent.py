import os
import time

class SelfEvolvingAgent:
    # ... (existing code)

    def detect_unused_files(self, directory, days_inactive=30):
        """Detect files that have not been accessed or modified in the given days"""
        unused_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_stat = os.stat(file_path)
                if time.time() - file_stat.st_atime > days_inactive * 24 * 60 * 60:
                    unused_files.append(file_path)
        return unused_files

    def delete_unused_files(self, unused_files):
        """Delete unused files"""
        for file in unused_files:
            try:
                os.remove(file)
                print(f"Deleted file: {file}")
            except Exception as e:
                print(f"Error deleting file: {file} - {e}")

    def run_cycle(self):
        # ... (existing code)
        directory = "."  # current directory
        unused_files = self.detect_unused_files(directory)
        self.delete_unused_files(unused_files)
        # ... (existing code)