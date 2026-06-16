import json

def read_config(path):
    try:
        with open(path, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error reading config: {e}")
        return None

def write_config(path, config):
    try:
        with open(path, 'w') as file:
            json.dump(config, file)
    except Exception as e:
        print(f"Error writing config: {e}")

def update_config(path, new_config):
    try:
        with open(path, 'r+') as file:
            config = json.load(file)
            config.update(new_config)
            file.seek(0)
            json.dump(config, file)
            file.truncate()
    except Exception as e:
        print(f"Error updating config: {e}")