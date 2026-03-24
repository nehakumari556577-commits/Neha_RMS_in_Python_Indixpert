from app.database.data import data
from app.menu.view_menu import ViewMenu

from app.order.create_order import CreateOrder
from app.order.order_history import OrderHistory


class StaffDashboard:

    def __init__(self, user):
        self.user = user
        self.menu_data = data()
        self.menu_file = "app/database/menu.json"
        self.order_file = "app/database/orders.json"
    
        self.view_menu_obj = ViewMenu()
        self.order_obj = CreateOrder()        
        self.history_obj = OrderHistory()     

    def start(self):
        while True:
            try:
                print("\n===== STAFF DASHBOARD =====")
                print("Welcome", self.user["name"])
                print("1 View Menu")
                print("2 Take Order")
                print("3 View Orders")
                print("4 Logout")

                choice = input("Enter choice: ")

                if not choice.isdigit():
                    print("Invalid Input")
                    continue

                choice = int(choice)

                if choice == 1:
                    self.view_menu_obj.show()

                elif choice == 2:
                    order = self.order_obj.create(self.user["name"])
                    if order:
                        print("Order Created Successfully!")

                elif choice == 3:
                    self.history_obj.show_orders() 

                elif choice == 4:
                    print("Logging out...")
                    break

                else:
                    print("Invalid Choice")

            except Exception as e:
                print("Error:", e)