def write_file(path, content):
    """
    Writes content to a file.

    Args:
        path (str): The path to the file.
        content (str): The content to write to the file.
    """
    try:
        with open(path, 'w') as file:
            file.write(content)
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
write_file('example.txt', 'Hello, world!')