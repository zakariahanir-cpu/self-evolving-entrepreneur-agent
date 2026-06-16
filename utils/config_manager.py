import json
import yaml

def read_config(path):
    """Read a configuration file."""
    with open(path, 'r') as file:
        if path.endswith('.json'):
            return json.load(file)
        elif path.endswith('.yaml') or path.endswith('.yml'):
            return yaml.safe_load(file)
        else:
            raise ValueError("Unsupported configuration file format")

def write_config(config, path):
    """Write a configuration to a file."""
    with open(path, 'w') as file:
        if path.endswith('.json'):
            json.dump(config, file, indent=4)
        elif path.endswith('.yaml') or path.endswith('.yml'):
            yaml.dump(config, file, default_flow_style=False)
        else:
            raise ValueError("Unsupported configuration file format")

def modify_config(config, path):
    """Modify a configuration file."""
    # Implement configuration modification logic here
    # For example, using the json or yaml libraries
    with open(path, 'r+') as file:
        if path.endswith('.json'):
            config = json.load(file)
            # Modify the config here
            file.seek(0)
            json.dump(config, file, indent=4)
            file.truncate()
        elif path.endswith('.yaml') or path.endswith('.yml'):
            config = yaml.safe_load(file)
            # Modify the config here
            file.seek(0)
            yaml.dump(config, file, default_flow_style=False)
            file.truncate()
        else:
            raise ValueError("Unsupported configuration file format")