import re

def fix_indentation(code):
    # Simple indentation fixer
    lines = code.split('\n')
    fixed_lines = []
    for line in lines:
        if line.strip().startswith('def') or line.strip().startswith('class'):
            fixed_lines.append('    ' + line)
        else:
            fixed_lines.append(line)
    return '\n'.join(fixed_lines)