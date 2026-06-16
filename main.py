from utils.fs_navigation import list_directories, create_directory, change_directory
from utils.file_io import read_file, write_file, append_file
from utils.script_generator import generate_script
from utils.config_manager import read_config, write_config, update_config

def main():
    # Example workflow
    create_directory("new_dir")
    change_directory("new_dir")
    generate_script("new_script")
    write_file("config.json", {"key": "value"})

if __name__ == '__main__':
    main()