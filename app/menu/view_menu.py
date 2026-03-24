from app.database.data import data

class ViewMenu:

    def __init__(self):
        self.data = data()
        self.menu_file = "app/database/menu.json"
        self.order_file = "app/database/orders.json"

    def show(self):

        menu = self.data.read(self.menu_file)

        if not menu:
            print("Menu is empty!")
            return

        categories = {
            "Breakfast": {"veg": [], "nonveg": []},
            "Lunch": {"veg": [], "nonveg": []},
            "Dinner": {"veg": [], "nonveg": []}
        }

        for item in menu:
            name = item["name"].lower()

            if "chicken" in name or "egg" in name:
                food_type = "nonveg"
            else:
                food_type = "veg"

            category = item.get("category", "Lunch")

            if category in categories:
                categories[category][food_type].append(item)

        print("\n" + "="*50)
        print("        RESTAURANT MENU        ")
        print("="*50)

        for cat, types in categories.items():

            print(f"\n\n {cat.upper()} MENU ")
            print("-"*50)


            print("\n----VEG ITEMS----:")
            if types["veg"]:
                for item in types["veg"]:
                    print(f"{item['id']:>2}. {item['name']:<25} ₹{item['half_price']}/{item['full_price']}")
            else:
                print("   No Veg items available")

    
            print("\n----NON-VEG ITEMS----:")
            if types["nonveg"]:
                for item in types["nonveg"]:
                    print(f"{item['id']:>2}. {item['name']:<25} ₹{item['half_price']}/{item['full_price']}")
            else:
                print("   No Non-Veg items available")

            print("\n" + "-"*50)

        print("\n" + "="*50)
        print("Half / Full prices shown as: ₹Half / ₹Full")
        print("="*50)