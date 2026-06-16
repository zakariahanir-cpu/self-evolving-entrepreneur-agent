import json
import os

def load_config(path):
    """Load a configuration file from the specified path."""
    with open(path, 'r') as f:
        return json.load(f)

def save_config(path, config):
    """Save a configuration to a file at the specified path."""
    with open(path, 'w') as f:
        json.dump(config, f, indent=4)

def update_config(path, new_config):
    """Update an existing configuration file at the specified path."""
    with open(path, 'w') as f:
        json.dump(new_config, f, indent=4)