import json

class ConfigParser:
    def __init__(self, config_file):
        self.config_file = config_file

    def parse_config(self):
        with open(self.config_file, 'r') as file:
            return json.load(file)

    def update_config(self, new_config):
        with open(self.config_file, 'w') as file:
            json.dump(new_config, file)