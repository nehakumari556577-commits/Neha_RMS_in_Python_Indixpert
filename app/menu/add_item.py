import json

class AddItem:

    def __init__(self):
        self.file = "app/database/menu.json"
        self.order_file = "app/database/orders.json"

    def add(self):
        try:
            with open(self.file, "r") as f:
                menu = json.load(f)
        except:
            menu = []

        print("\n===== ADD NEW ITEM =====")

        if menu:
            new_id = menu[-1]["id"] + 1
        else:
            new_id = 1

        name = input("Enter Item Name: ").strip()

        category = input("Enter Category (Lunch/Dinner/Fast Food): ").strip()

        while True:
            half_price = input("Enter Half Price: ")
            if half_price.isdigit():
                half_price = int(half_price)
                break
            else:
                print("Invalid price!")

        while True:
            full_price = input("Enter Full Price: ")
            if full_price.isdigit():
                full_price = int(full_price)
                break
            else:
                print("Invalid price!")

        new_item = {
            "id": new_id,
            "name": name,
            "half_price": half_price,
            "full_price": full_price,
            "category": category
        }

        menu.append(new_item)

        with open(self.file, "w") as f:
            json.dump(menu, f, indent=4)

        print("Item Added Successfully!")