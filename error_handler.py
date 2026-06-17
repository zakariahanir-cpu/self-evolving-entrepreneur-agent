import logging
import ast

class ErrorHandler:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def catch_error(self, error):
        self.logger.error(error)
        # parse code and patch error

    def read_logs(self, log_file):
        with open(log_file, "r") as f:
            logs = f.readlines()
        return logs

    def patch_code(self, code, error):
        # use ast to parse code and patch error
        pass