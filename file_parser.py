import ast

def parse_python_file(path):
    """Parse a Python file and return an abstract syntax tree (AST)."""
    with open(path, 'r') as file:
        return ast.parse(file.read())

def generate_python_file(path, ast):
    """Generate a Python file from an AST."""
    with open(path, 'w') as file:
        file.write(ast.unparse())