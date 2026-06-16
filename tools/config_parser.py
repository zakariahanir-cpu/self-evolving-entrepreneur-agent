import json

def parse_config(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Invalid JSON: {file_path}")
        return None

def update_config(file_path, new_config):
    try:
        with open(file_path, 'w') as file:
            json.dump(new_config, file)
    except Exception as e:
        print(f"Error updating config: {e}")