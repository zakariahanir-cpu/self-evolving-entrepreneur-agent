import json

class Config:
    def __init__(self, path):
        self.path = path
        self.load()

    def load(self):
        """Load configuration from file."""
        if os.path.exists(self.path):
            with open(self.path, 'r') as file:
                self.config = json.load(file)
        else:
            self.config = {}

    def save(self):
        """Save configuration to file."""
        with open(self.path, 'w') as file:
            json.dump(self.config, file)

    def get(self, key):
        """Get a configuration value."""
        return self.config.get(key)

    def set(self, key, value):
        """Set a configuration value."""
        self.config[key] = value
        self.save()