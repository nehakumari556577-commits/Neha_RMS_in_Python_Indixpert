from app.database.data import data
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

class Login:    
    def __init__(self):
        self.data = data()
        self.file = "app/database/users.json"

    def login(self):

        print("\n********* LOGIN **********")
        users = self.data.read(self.file)

        if users is None:       
            users = []

        while True:
            email = input("Please Enter Your Email: ")

            if "@" not in email or "." not in email:
                print("Invalid Email Format")
            else:
                break
        
        while True:
            password = input_password("Please Enter Your Password: ")

            if not password.isalnum():
                print("Password must be alphanumeric")
                continue

            if len(password) < 6:
                print("Password must be at least 6 characters")
                continue
            
            for u in users:
                if u["email"] == email and u["password"] == password:
                    print("Login Successfully")
                    return u
            print("Invalid Email or Password")
            
                    