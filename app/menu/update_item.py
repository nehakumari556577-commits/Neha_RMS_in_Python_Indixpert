import json

class UpdateItem:

    def __init__(self):
        self.file = "app/database/menu.json"
        self.order_file = "app/database/orders.json"

    def update(self):
        try:
            with open(self.file, "r") as f:
                menu = json.load(f)
        except:
            print("Menu not found!")
            return

        if not menu:
            print("Menu is empty!")
            return

        print("\n===== UPDATE ITEM =====")

        for item in menu:
            print(f"{item['id']}. {item['name']} - ₹{item['half_price']}/₹{item['full_price']} ({item['category']})")

        
        item_id = input("Enter Item ID to update: ")

        if not item_id.isdigit():
            print("Invalid ID!")
            return

        item_id = int(item_id)


        found = False
        for item in menu:
            if item["id"] == item_id:
                found = True

                print(f"\nUpdating: {item['name']}")

                name = input("Enter new name (leave blank to keep same): ").strip()
                if name:
                    item["name"] = name

                category = input("Enter new category (leave blank to keep same): ").strip()
                if category:
                    item["category"] = category

                half_price = input("Enter new half price (leave blank to keep same): ")
                if half_price:
                    if half_price.isdigit():
                        item["half_price"] = int(half_price)
                    else:
                        print("Invalid half price!")

                full_price = input("Enter new full price (leave blank to keep same): ")
                if full_price:
                    if full_price.isdigit():
                        item["full_price"] = int(full_price)
                    else:
                        print("Invalid full price!")

                break

        if not found:
            print("Item not found!")
            return
        with open(self.file, "w") as f:
            json.dump(menu, f, indent=4)

        print("Item Updated Successfully!")