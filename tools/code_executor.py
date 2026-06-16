import subprocess

class CodeExecutor:
    def __init__(self):
        pass

    def execute_script(self, script):
        try:
            output = subprocess.check_output(['python', '-c', script])
            return output.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return str(e)