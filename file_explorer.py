import os

def list_files(directory):
    """
    Lists the files and directories in a given directory.

    Args:
        directory (str): The path to the directory.

    Returns:
        list: A list of files and directories in the directory.
    """
    try:
        return os.listdir(directory)
    except FileNotFoundError:
        return "Directory not found."

# Example usage:
print(list_files('.'))