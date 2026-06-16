import json

def read_config_file(file_path):
    with open(file_path, 'r') as file:
        config = json.load(file)
        return config