import fs_interaction

class ScriptGenerator:
    def __init__(self, path):
        self.path = path

    def generate_script(self, content):
        """Generate a new Python script."""
        fs_interaction.write_file(self.path, content)

    def modify_script(self, new_content):
        """Modify an existing Python script."""
        fs_interaction.modify_file(self.path, new_content)