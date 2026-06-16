import ast

def validate_file(file_path):
    """
    Validate the syntax and content of a Python script.
    
    Args:
        file_path (str): The path to the file to validate.
    
    Returns:
        bool: True if the file is valid, False otherwise.
    """
    try:
        with open(file_path, "r") as file:
            content = file.read()
            ast.parse(content)
            return True
    except SyntaxError:
        return False

def main():
    file_path = "example.py"  # example file
    if validate_file(file_path):
        print("File is valid.")
    else:
        print("File is invalid.")

if __name__ == "__main__":
    main()