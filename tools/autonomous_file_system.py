import json
from utils.file_system import create_directory, delete_file, copy_file

def load_config(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def execute_operations(config):
    for operation in config['operations']:
        if operation['type'] == 'create_directory':
            create_directory(operation['path'])
        elif operation['type'] == 'delete_file':
            delete_file(operation['path'])
        elif operation['type'] == 'copy_file':
            copy_file(operation['src'], operation['dst'])

def main():
    config_file = 'config.json'
    config = load_config(config_file)
    execute_operations(config)

if __name__ == '__main__':
    main()