from app.database.data import data
from app.logs.logger import Logger

class ViewMenu:

    def __init__(self):
        self.data = data()
        self.menu_file = "app/database/menu.json"
        self.logger = Logger()  

    def show_menu(self):
        try:
            menu = self.data.read(self.menu_file)

            if not menu:
                print("Menu is empty")
                return

            if not isinstance(menu, list):
                print("Invalid menu data")
                return

            categories = ["Breakfast", "Lunch", "Dinner"]

            print("\n" + "="*70)
            print(" " * 25 + "RESTAURANT MENU")
            print("="*70)

            for category in categories:
                print(f"\n {category.upper()} MENU")
                print("-"*66)

                veg_items = [
                    i for i in menu
                    if i.get("category", "").lower() == category.lower()
                    and i.get("type", "").lower() == "veg"
                ]

                nonveg_items = [
                    i for i in menu
                    if i.get("category", "").lower() == category.lower()
                    and i.get("type", "").lower() == "non-veg"
                ]

                if veg_items:
                    print("\n VEG ITEMS")
                    self.print_table(veg_items)

                if nonveg_items:
                    print("\n NON-VEG ITEMS")
                    self.print_table(nonveg_items)

        except Exception as e:
            self.logger.log_error(f"ViewMenu.show_menu Error: {str(e)}")
            print("Error in View Menu. Check log for details.")

    def print_table(self, items):
        try:
            print("+----+----------------------+----------+----------+")
            print("| ID | Item Name            | Half ₹   | Full ₹   |")
            print("+----+----------------------+----------+----------+")

            for item in items:
                item_id = str(item.get('id', 'N/A')).ljust(2)
                name = str(item.get('name', 'N/A')).ljust(20)
                half_price = f"₹{str(item.get('half_price', 'N/A'))}".ljust(8)
                full_price = f"₹{str(item.get('full_price', 'N/A'))}".ljust(8)

                print(f"| {item_id} | {name} | {half_price} | {full_price} |")

            print("+----+----------------------+----------+----------+")

        except Exception as e:
            self.logger.log_error(f"ViewMenu.print_table Error: {str(e)}")
            print("Error printing table. Check log for details.")