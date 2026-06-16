import configparser

def parse_config_file(path):
    """Parse a configuration file."""
    config = configparser.ConfigParser()
    config.read(path)
    return config

def update_config_file(path, config):
    """Update a configuration file."""
    with open(path, 'w') as file:
        config.write(file)