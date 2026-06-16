import os
import subprocess

def run_script(script_path):
    try:
        subprocess.run(['python', script_path])
    except Exception as e:
        print(f"Error running script: {e}")