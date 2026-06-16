import os

def generate_script(template_path, output_path, params):
    try:
        with open(template_path, 'r') as template_file:
            template_content = template_file.read()
            for key, value in params.items():
                template_content = template_content.replace(f"{{{{ {key} }}}}", value)
            with open(output_path, 'w') as output_file:
                output_file.write(template_content)
    except Exception as e:
        print(f"Error: {e}")