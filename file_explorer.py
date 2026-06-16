import os

def explore_directory(directory):
    """
    Explore the directory and its subdirectories for Python scripts and configuration files.
    
    Args:
        directory (str): The path to the directory to explore.
    
    Returns:
        list: A list of Python scripts and configuration files found in the directory and its subdirectories.
    """
    python_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py") or file.endswith(".config"):
                python_files.append(os.path.join(root, file))
    return python_files

def main():
    directory = "."  # current directory
    python_files = explore_directory(directory)
    print("Python scripts and configuration files found:")
    for file in python_files:
        print(file)

if __name__ == "__main__":
    main()