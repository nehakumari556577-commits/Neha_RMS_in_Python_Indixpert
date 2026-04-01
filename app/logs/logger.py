import os
from datetime import datetime

class Logger:
    def __init__(self, log_file=None):

        if log_file is None:
            log_file = "error_log.txt" 
        self.log_file = log_file

    def log_error(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        try:
            with open(self.log_file, "a") as f:
                f.write(log_entry)
        except Exception as e:
            print("Logger failed to write:", e)


logger = Logger()
logger.log_error("Test error message")
print(f"Log file path: {os.path.abspath(logger.log_file)}")