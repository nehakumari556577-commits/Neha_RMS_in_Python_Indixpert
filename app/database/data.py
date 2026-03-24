import json
import os

class data:

    def read(self, file):
        if not os.path.exists(file):
            return []

        with open(file, "r") as f:
            try:
                return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                return []

    def write(self, file, data):
        with open(file, "w") as f:
            json.dump(data, f, indent=4)
