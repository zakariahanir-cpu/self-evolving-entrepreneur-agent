import os

class ScriptGenerator:
    def __init__(self, template_dir):
        self.template_dir = template_dir

    def generate_script(self, script_name, template_name):
        template_path = os.path.join(self.template_dir, template_name)
        with open(template_path, 'r') as template_file:
            template_content = template_file.read()
        script_path = os.path.join(self.template_dir, script_name)
        with open(script_path, 'w') as script_file:
            script_file.write(template_content)