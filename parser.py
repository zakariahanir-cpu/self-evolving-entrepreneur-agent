import ast

def parse_python_script(file_path):
    with open(file_path, 'r') as file:
        tree = ast.parse(file.read())
        functions = [node.name for node in tree.body if isinstance(node, ast.FunctionDef)]
        classes = [node.name for node in tree.body if isinstance(node, ast.ClassDef)]
        return functions, classes