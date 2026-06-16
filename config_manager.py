import json

def read_config(path):
    with open(path, 'r') as file:
        return json.load(file)

def write_config(path, config):
    with open(path, 'w') as file:
        json.dump(config, file)

def create_config(path, config):
    with open(path, 'w') as file:
        json.dump(config, file)

def modify_config(path, new_config):
    with open(path, 'w') as file:
        json.dump(new_config, file)