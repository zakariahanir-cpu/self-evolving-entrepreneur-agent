def generate_python_code(function_name, function_body):
    code = f'def {function_name}():\n'
    code += '    ' + '\n    '.join(function_body.split('\n'))
    return code