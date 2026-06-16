import os

def generate_script(template_path, output_path, placeholders):
    """Generate a Python script from a template."""
    with open(template_path, 'r') as template_file:
        template = template_file.read()
    for key, value in placeholders.items():
        template = template.replace(f'{{{{ {key} }}}}', value)
    with open(output_path, 'w') as output_file:
        output_file.write(template)