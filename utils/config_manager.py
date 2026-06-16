import json

def create_config_file(path, config):
    with open(path, 'w') as f:
        json.dump(config, f)

def read_config_file(path):
    with open(path, 'r') as f:
        return json.load(f)

def update_config_file(path, config):
    with open(path, 'w') as f:
        json.dump(config, f)

def delete_config_file(path):
    os.remove(path)