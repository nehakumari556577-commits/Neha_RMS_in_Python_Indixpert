import json

class DeleteItem:

    def __init__(self):
        self.file = "app/database/menu.json"
        self.order_file = "app/database/orders.json"

    def delete(self):
        try:
            with open(self.file, "r") as f:
                menu = json.load(f)
        except:
            print("Menu not found!")
            return

        if not menu:
            print("Menu is empty!")
            return

        print("\n===== DELETE ITEM =====")

        for item in menu:
            print(f"{item['id']}. {item['name']} - ₹{item['half_price']}/₹{item['full_price']} ({item['category']})")

        item_id = input("Enter Item ID to delete: ")

        if not item_id.isdigit():
            print("Invalid ID!")
            return

        item_id = int(item_id)

        found = False
        new_menu = []

        for item in menu:
            if item["id"] == item_id:
                found = True
                print(f"Deleting: {item['name']}")
            else:
                new_menu.append(item)

        if not found:
            print("Item not found!")
            return
        
        with open(self.file, "w") as f:
            json.dump(new_menu, f, indent=4)

        print("Item Deleted Successfully!")