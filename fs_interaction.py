import os

def read_file(path):
    with open(path, 'r') as file:
        return file.read()

def write_file(path, content):
    with open(path, 'w') as file:
        file.write(content)

def modify_file(path, new_content):
    with open(path, 'w') as file:
        file.write(new_content)

def main():
    # Example usage:
    path = 'example.txt'
    content = 'Hello, World!'
    write_file(path, content)
    print(read_file(path))

if __name__ == '__main__':
    main()