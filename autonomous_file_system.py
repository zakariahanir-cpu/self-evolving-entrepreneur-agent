from filesystem.interface import FileSystemInterface
from script_generator import ScriptGenerator

class AutonomousFileSystem:
    def __init__(self, root_dir, template_dir):
        self.root_dir = root_dir
        self.template_dir = template_dir
        self.file_system = FileSystemInterface(root_dir)
        self.script_generator = ScriptGenerator(template_dir, root_dir)

    def read_config_file(self, file_path):
        return self.file_system.read_file(file_path)

    def update_config_file(self, file_path, content):
        self.file_system.write_file(file_path, content)

    def create_script(self, template_name, params):
        self.script_generator.generate_script(template_name, params)