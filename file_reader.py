def read_file(path):
    """
    Reads the contents of a file.

    Args:
        path (str): The path to the file.

    Returns:
        str: The contents of the file.
    """
    try:
        with open(path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."

# Example usage:
print(read_file('example.txt'))