import json

def parse_config(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None

def modify_config(file_path, new_config):
    try:
        with open(file_path, 'w') as file:
            json.dump(new_config, file)
    except Exception as e:
        print(f"Error: {e}")