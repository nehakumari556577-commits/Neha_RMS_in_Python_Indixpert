from app.database.data import data
from app.logs.logger import Logger
import msvcrt


def input_password(prompt="Password: ", logger=None):
    """
    Custom password input with masking (*)
    Logs any errors if logger is provided
    """
    try:
        print(prompt, end="", flush=True)
        password = ""

        while True:
            char = msvcrt.getch()

            if char in {b'\r', b'\n'}:
                print("")
                break
            elif char == b'\x08': 
                if len(password) > 0:
                    password = password[:-1]
                    print("\b \b", end="", flush=True)
            else:
                password += char.decode("utf-8")
                print("*", end="", flush=True)

        return password

    except Exception as e:
        if logger:
            logger.log_error(f"Password Input Error: {str(e)}")
        print("Password Input Error:", e)
        return ""


class Login:
    def __init__(self):
        self.data = data()
        self.file = "app/database/users.json"
        self.logger = Logger()

    def login(self):
        try:
            print("\n********* LOGIN **********")

            users = self.data.read(self.file) or []
            while True:
                email = input("Please Enter Your Email: ").strip()
                if "@" not in email or "." not in email:
                    print("Invalid Email Format")
                    continue
                break

            while True:
                password = input_password("Please Enter Your Password: ", logger=self.logger)

                if not password.isalnum():
                    print("Password must be alphanumeric")
                    continue
                if len(password) < 6:
                    print("Password must be at least 6 characters")
                    continue

                for u in users:
                    if u.get("email") == email and u.get("password") == password:
                        print("Login Successful!")
                        return u

                print("Invalid Email or Password")

        except Exception as e:
            self.logger.log_error(f"Login Error: {str(e)}")
            print("Login Error:", e)