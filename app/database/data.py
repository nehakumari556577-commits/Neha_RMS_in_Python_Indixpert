import json
from app.logs.logger import Logger  

class data:
    def __init__(self):
        self.logger = Logger()  

    def read(self, file_path):
        try:
            with open(file_path, "r") as f:
                return json.load(f)
        except Exception as e:
            self.logger.log_error(f"Read Error in {file_path}: {str(e)}")
            return [] 

    def write(self, file_path, data_to_write):
        try:
            with open(file_path, "w") as f:
                json.dump(data_to_write, f, indent=4)
        except Exception as e:
            self.logger.log_error(f"Write Error in {file_path}: {str(e)}")