import json

class ConfigManager:
    def __init__(self, config_file):
        self.config_file = config_file

    def read_config(self):
        with open(self.config_file, 'r') as file:
            return json.load(file)

    def write_config(self, config):
        with open(self.config_file, 'w') as file:
            json.dump(config, file, indent=4)