import fs_module

class ScriptGenerator:
    def __init__(self):
        pass

    def generate_script(self, template, params):
        script = template.format(**params)
        return script

    def save_script(self, script, file_path):
        fs_module.write_file(file_path, script)