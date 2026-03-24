from app.auth.sign_up import Signup
from app.auth.login import Login
from app.dashboard.Admin_dashboard import AdminDashboard
from app.dashboard.staff_dashboard import StaffDashboard

signup_obj = Signup()
login_obj = Login()

def manage_menu():

    while True:
        print('-'*40)
        print("\n===== RESTAURANT MANAGEMENT SYSTEM =====")
        print("1 Signup")
        print("2 Login")
        print("3 Exit")
        print('-'*40)

        choice = input("Please Enter Your Choice: ")

        if not choice.isdigit():
            print("Invalid input")
            continue

        choice = int(choice)

        if choice == 1:
            signup_obj.signup()

        elif choice == 2: 
            user = login_obj.login()

            if user:  

                if user["role"] == "admin":
                    admin = AdminDashboard(user)
                    admin.start()

                elif user["role"] == "staff":
                    staff = StaffDashboard(user) 
                    staff.start()

            else:
                print("Invalid Email or Password!")

        elif choice == 3:
            print("Exiting...")
            break

        else:
            print("Invalid choice")