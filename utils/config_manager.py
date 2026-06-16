import json

def read_config(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def write_config(file_path, config):
    with open(file_path, 'w') as file:
        json.dump(config, file, indent=4)

def update_config(file_path, key, value):
    config = read_config(file_path)
    config[key] = value
    write_config(file_path, config)