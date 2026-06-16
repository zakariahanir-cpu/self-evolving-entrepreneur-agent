import json
import yaml
import configparser

class ConfigParser:
    def __init__(self):
        pass

    def parse_json(self, file_path):
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return None

    def parse_yaml(self, file_path):
        try:
            with open(file_path, 'r') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            return None

    def parse_ini(self, file_path):
        config = configparser.ConfigParser()
        config.read(file_path)
        return config