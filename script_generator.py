import os
from filesystem.interface import FileSystemInterface

class ScriptGenerator:
    def __init__(self, template_dir, output_dir):
        self.template_dir = template_dir
        self.output_dir = output_dir
        self.file_system = FileSystemInterface(output_dir)

    def generate_script(self, template_name, params):
        template_path = os.path.join(self.template_dir, template_name)
        template_content = self.file_system.read_file(template_path)

        if template_content:
            script_content = self.replace_params(template_content, params)
            script_name = f"{template_name.split('.')[0]}_{params['name']}.py"
            self.file_system.create_file(script_name, script_content)
        else:
            print(f"Template not found: {template_name}")

    def replace_params(self, template_content, params):
        for key, value in params.items():
            template_content = template_content.replace(f"{{{{ {key} }}}}", value)
        return template_content