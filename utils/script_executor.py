import subprocess

def execute_script(path):
    try:
        subprocess.run(['python', path])
    except Exception as e:
        print(f"Error executing script: {e}")