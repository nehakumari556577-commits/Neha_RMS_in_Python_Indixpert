import json
import datetime

class OrderHistory:

    def __init__(self):
        self.menu_file = "app/database/menu.json"
        self.order_file = "app/database/orders.json"

    def save_order(self, order):

        try:
            with open(self.order_file, "r") as f:
                orders = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            orders = []

        
        order_id = max([o.get("order_id", 0) for o in orders], default=0) + 1

        order_data = {
            "order_id": order_id,
            "staff_name": order["staff_name"],
            "items": order["items"],
            "total": order["total"],
            "timestamp": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "status": "Completed"
        }

        orders.append(order_data)

        with open(self.order_file, "w") as f:
            json.dump(orders, f, indent=4)

        print("Order saved to history!")

    def show_orders(self):

        try:
            with open(self.order_file, "r") as f:
                orders = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print(" No order history found!")
            return

        if not orders:
            print(" No orders yet!")
            return

        for order in orders:
            print("\n===== ORDER =====")
            print(f"Order ID: {order.get('order_id')}")
            print(f"Staff: {order.get('staff_name')}")
            print(f"Time: {order.get('timestamp')}")
            print("Items:")

            for item in order.get("items", []):
                print(f"{item.get('name')} ({item.get('size')}) x {item.get('quantity')} = ₹{item.get('total')}")

            print(f"Total: ₹{order.get('total')}")
            print(f"Status: {order.get('status')}")