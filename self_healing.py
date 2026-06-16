import paramiko

class SelfHealing:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.ssh_client = paramiko.SSHClient()

    def connect(self):
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_client.connect(self.host, username=self.username, password=self.password)

    def deploy_patch(self, patch):
        stdin, stdout, stderr = self.ssh_client.exec_command(patch)
        return stdout.read().decode()