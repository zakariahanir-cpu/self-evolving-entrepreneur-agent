import configparser

def read_config(file_path):
    """Read a configuration file at the specified path."""
    config = configparser.ConfigParser()
    config.read(file_path)
    return config

def write_config(file_path, config):
    """Write a configuration to a file at the specified path."""
    with open(file_path, 'w') as f:
        config.write(f)