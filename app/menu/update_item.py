from app.database.data import data
from app.logs.logger import Logger

class UpdateMenuItem:

    def __init__(self):
        self.data = data()
        self.menu_file = "app/database/menu.json"
        self.logger = Logger()  

    def update_item(self):
        try:
            menu = self.data.read(self.menu_file) or []

            try:
                item_id = int(input("Enter Item ID to update: "))
            except ValueError:
                print("Invalid ID. Must be a number!")
                return

            for item in menu:
                if item["id"] == item_id:

                    print(f"\nUpdating: {item['name']}")

                    new_name = input("New Name (leave blank to skip): ").strip()
                    new_half = input("New Half Price (leave blank to skip): ").strip()
                    new_full = input("New Full Price (leave blank to skip): ").strip()

                    if new_name:
                        item["name"] = new_name

                    if new_half.isdigit():
                        item["half_price"] = int(new_half)

                    if new_full.isdigit():
                        item["full_price"] = int(new_full)

                    self.data.write(self.menu_file, menu)
                    print("Item Updated Successfully!")
                    return

            print("Item not found!")

        except Exception as e:
            self.logger.log_error(f"UpdateMenuItem Error: {str(e)}")
            print("An error occurred. Check log for details.")