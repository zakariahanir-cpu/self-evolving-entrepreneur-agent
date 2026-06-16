import os

def explore_file_system(root_dir):
    python_files = []
    config_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
            elif file.endswith(".config"):
                config_files.append(os.path.join(root, file))
    return python_files, config_files