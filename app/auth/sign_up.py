from app.database.data import data
import uuid
import msvcrt

def input_password(prompt="Password: "):
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

class Signup:
    def __init__(self):
        self.data = data()
        self.file = "app/database/users.json"

    def signup(self):

        users = self.data.read(self.file)
        if users is None:
            users = []

        print("\n******** SIGNUP ********")

        user_id = str(uuid.uuid4())

        while True:
            name = input("Please Enter Your Name: ").strip()

            if not name.replace(" ", "").isalpha():
                print("Please enter only letters")
                continue

            break  

        while True:
            email = input("Please Enter Your Email: ").strip()

            if "@" not in email or "." not in email:
                print("Invalid Email format")
                continue  

            for user in users:
                if user["email"] == email:
                    print("Email already registered")
                    return   
            break   
        while True:
            password = input_password("Please Enter Your Password: ")
            confirm = input_password("Confirm Your Password: ")

            if password != confirm:
                print("Passwords do not match")
                continue

            if not password.isalnum():
                print("Please enter only letters and numbers")
                continue

            if len(password) < 6:
                print("Password must be at least 6 characters")
                continue

            break

        role = "staff"

        new_user = {
            "user_id": user_id,
            "name": name,
            "email": email,
            "password": password,
            "role": role
        }

        users.append(new_user)
        self.data.write(self.file, users)

        print("Signup Successful ")