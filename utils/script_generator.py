def generate_script(script_name):
    script_template = """
# Python script template
def main():
    pass

if __name__ == '__main__':
    main()
"""
    with open(f"{script_name}.py", 'w') as file:
        file.write(script_template)