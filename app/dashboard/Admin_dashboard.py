from app.database.data import data
from app.menu.add_item import AddItem 
from app.menu.view_menu import ViewMenu
from app.menu.update_item import UpdateItem
from app.menu.delete_item import DeleteItem

class AdminDashboard:

    def __init__(self, user):
        self.user = user
        self.menu_data = data()
        self.menu_file = "app/database/menu.json"
        self.order_file = "app/database/orders.json"
        
        self.add_item_obj = AddItem()
        self.view_menu_obj = ViewMenu()
        self.update_item_obj = UpdateItem()
        self.delete_item_obj = DeleteItem()

    def start(self):
        while True:
            try:
                print("\n===== ADMIN DASHBOARD =====")
                print("Welcome", self.user["name"])
                print("1 Manage Menu")
                print("2 Manage Orders")
                print("3 Reports")
                print("4 Logout")

                choice = input("Enter choice: ")

                if not choice.isdigit():
                    print("Invalid Input")
                    continue

                choice = int(choice)

                if choice == 1:
                    self.manage_menu()

                elif choice == 2:
                    print("Order Management (coming soon)")

                elif choice == 3:
                    print("Reports (coming soon)")

                elif choice == 4:
                    print("Logging out...")
                    break

                else:
                    print("Invalid Choice")

            except Exception as e:
                print("Error:", e)

    def manage_menu(self):
        while True:
            try:
                print("\n===== MENU MANAGEMENT =====")
                print("1 Add Item")
                print("2 View Menu")
                print("3 Update Item")
                print("4 Delete Item")
                print("5 Back")

                choice = input("Enter choice: ")

                if not choice.isdigit():
                    print("Invalid Input")
                    continue

                choice = int(choice)

                if choice == 1:
                    self.add_item_obj.add()

                elif choice == 2:
                    self.view_menu_obj.show()

                elif choice == 3:
                    self.update_item_obj.update()

                elif choice == 4:
                    self.delete_item_obj.delete()

                elif choice == 5:
                    break

                else:
                    print("Invalid Choice")

            except Exception as e:
                print("Error:", e)