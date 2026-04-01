from app.database.data import data
from app.menu.view_menu import ViewMenu
from app.order.create_order import CreateOrder
from app.order.view_orders import ViewOrder
from app.billing.generate_bill import GenerateBill
from app.booking.create_booking import CreateBooking
from app.logs.logger import Logger


class StaffDashboard:

    def __init__(self, user):
        self.user = user
        self.data = data()
        self.logger = Logger() 

        self.view_menu_obj = ViewMenu()
        self.create_order_obj = CreateOrder()
        self.view_order_obj = ViewOrder()
        self.generate_bill_obj = GenerateBill()
        self.create_booking_obj = CreateBooking()

    def start(self):
        while True:
            try:
                print("\n" + "=" * 70)
                print("STAFF DASHBOARD".center(70))
                print("=" * 70)

                print(f"User : {self.user.get('name', 'Staff')}")
                print("-" * 70)

                print("1. Create Booking")
                print("2. View Menu")
                print("3. Take Order")
                print("4. View Orders")
                print("5. Generate Bill")
                print("6. Logout")
                print("-" * 70)

                choice = input("Enter choice: ").strip()

                if not choice.isdigit():
                    print("Invalid input. Enter a number between 1-6.")
                    continue

                choice = int(choice)

                if choice == 1:
                    self.create_booking_obj.create()

                elif choice == 2:
                    self.view_menu_obj.show_menu()

                elif choice == 3:
                    self.create_order_obj.create(self.user["name"])

                elif choice == 4:
                    self.view_order_obj.view_orders()

                elif choice == 5:
                    self.generate_bill_obj.generate()

                elif choice == 6:
                    print("Logging out...")
                    break

                else:
                    print("Invalid choice. Enter a number between 1-6.")

            except Exception as e:
                self.logger.log_error(f"StaffDashboard Error: {str(e)}")
                print("Error occurred. Check log.")