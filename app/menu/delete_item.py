from app.database.data import data
from app.logs.logger import Logger

class DeleteMenuItem:

    def __init__(self):
        self.data = data()
        self.menu_file = "app/database/menu.json"
        self.logger = Logger()  

    def delete_item(self):
        try:
            menu = self.data.read(self.menu_file) or []

            try:
                item_id = int(input("Enter Item ID to delete: "))
            except ValueError:
                print("Invalid ID. Must be a number!")
                return

            new_menu = [item for item in menu if item["id"] != item_id]

            if len(menu) == len(new_menu):
                print("Item not found!")
            else:
                self.data.write(self.menu_file, new_menu)
                print("Item Deleted Successfully!")

        except Exception as e:
            self.logger.log_error(f"DeleteMenuItem Error: {str(e)}")
            print("An error occurred. Check log for details.")