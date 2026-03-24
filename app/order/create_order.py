from app.database.data import data
from datetime import datetime

class CreateOrder:

    def __init__(self):
        self.data = data()
        self.menu_file = "app/database/menu.json"
        self.order_file = "app/database/orders.json"

    def create(self, staff_name):

        menu = self.data.read(self.menu_file)
        orders = self.data.read(self.order_file)

        if orders is None:
            orders = []

        print("\n------ MENU ------")
        for item in menu:
            print(f"{item['id']}. {item['name']} - Half ₹{item['half_price']} | Full ₹{item['full_price']}")

        order_items = []
        total = 0

        while True:
            try:
                item_id = int(input("\nEnter Item ID (0 to finish): "))
            except ValueError:
                print("Invalid input!")
                continue

            if item_id == 0:
                break

            selected_item = next((i for i in menu if i["id"] == item_id), None)

            if not selected_item:
                print("Item not found!")
                continue

            choice = input("Half or Full? (h/f): ").lower()

            if choice == 'h':
                price = selected_item["half_price"]
                size = "Half"
            elif choice == 'f':
                price = selected_item["full_price"]
                size = "Full"
            else:
                print("Invalid choice!")
                continue

            try:
                qty = int(input("Enter Quantity: "))
            except ValueError:
                print("Invalid quantity!")
                continue

            item_total = price * qty
            total += item_total

            order_items.append({
                "item_id": selected_item["id"],
                "name": selected_item["name"],
                "size": size,
                "price": price,
                "quantity": qty,
                "total": item_total
            })

            print("Item added!")

        if not order_items:
            print("No order created.")
            return None

        order_id = len(orders) + 1

        order_data = {
            "order_id": order_id,
            "staff_name": staff_name,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "items": order_items,
            "total": total
        }

        orders.append(order_data)
        self.data.write(self.order_file, orders)

        print("Order saved!")

        return order_data