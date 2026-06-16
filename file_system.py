import os
import json

def read_file(path):
    with open(path, 'r') as file:
        return file.read()

def modify_file(path, content):
    with open(path, 'w') as file:
        file.write(content)

def create_file(path, content):
    with open(path, 'w') as file:
        file.write(content)

def parse_config_file(path):
    with open(path, 'r') as file:
        return json.load(file)

def update_config_file(path, config):
    with open(path, 'w') as file:
        json.dump(config, file)