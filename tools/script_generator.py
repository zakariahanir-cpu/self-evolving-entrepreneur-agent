import ast

class ScriptGenerator:
    def __init__(self):
        self.template = """
print("Hello, World!")
"""

    def generate_script(self, script_name):
        script = self.template.replace("Hello, World!", script_name)
        return script