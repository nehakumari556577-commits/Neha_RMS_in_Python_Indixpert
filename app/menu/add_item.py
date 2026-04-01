from app.database.data import data
from app.logs.logger import Logger

class AddMenuItem:

    def __init__(self):
        self.data = data()
        self.menu_file = "app/database/menu.json"
        self.logger = Logger() 

    def add_item(self):
        menu = self.data.read(self.menu_file) or []

        try:
            print("\n===== ADD NEW ITEM =====")

            name = input("Enter Item Name: ").strip()

            try:
                half_price = int(input("Enter Half Price: "))
                full_price = int(input("Enter Full Price: "))
            except ValueError:
                print("Price must be a number!")
                return

            category = input("Enter Category (Breakfast/Lunch/Dinner): ").strip()
            item_type = input("Enter Type (Veg/Non-Veg): ").strip()

        
            new_id = max([item["id"] for item in menu], default=0) + 1

            new_item = {
                "id": new_id,
                "name": name,
                "half_price": half_price,
                "full_price": full_price,
                "category": category,
                "type": item_type
            }

            menu.append(new_item)
            self.data.write(self.menu_file, menu)

            print("Item Added Successfully!")

        except Exception as e:
            self.logger.log_error(f"AddMenuItem Error: {str(e)}")
            print("An error occurred. Check log for details.")