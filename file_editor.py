import os

def read_file(file_path):
    """
    Read the content of a file.
    
    Args:
        file_path (str): The path to the file to read.
    
    Returns:
        str: The content of the file.
    """
    with open(file_path, "r") as file:
        return file.read()

def write_file(file_path, content):
    """
    Write content to a file.
    
    Args:
        file_path (str): The path to the file to write.
        content (str): The content to write to the file.
    """
    with open(file_path, "w") as file:
        file.write(content)

def main():
    file_path = "example.py"  # example file
    content = "print('Hello World')"
    write_file(file_path, content)
    print("File created/modified successfully.")

if __name__ == "__main__":
    main()