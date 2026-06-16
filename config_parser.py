import json

def parse_config(path):
    with open(path, 'r') as file:
        return json.load(file)

def main():
    # Example usage:
    path = 'config.json'
    config = parse_config(path)
    print(config)

if __name__ == '__main__':
    main()