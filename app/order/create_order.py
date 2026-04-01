from app.database.data import data
from datetime import datetime
from app.logs.logger import Logger

class CreateOrder:

    def __init__(self):
        self.data = data()
        self.menu_file = "app/database/menu.json"
        self.order_file = "app/database/orders.json"
        self.report_file = "app/database/report.json"
        self.logger = Logger()

    def create(self, staff_name):
        try:
            menu = self.data.read(self.menu_file) or []
            orders = self.data.read(self.order_file) or []
            report = self.data.read(self.report_file) or []

            if not menu:
                print("\nMenu not available!")
                return

            order_items = []
            total = 0

            print("\n" + "=" * 60)
            print(" " * 20 + "TAKE ORDER")
            print("=" * 60)

            print("\nAvailable Items:")
            print("+----+----------------------+----------+----------+")
            print("| ID | Item Name            | Half ₹   | Full ₹   |")
            print("+----+----------------------+----------+----------+")

            for item in menu:
                print(f"| {str(item['id']).ljust(2)} "
                      f"| {item['name'].ljust(20)} "
                      f"| {str(item['half_price']).ljust(8)} "
                      f"| {str(item['full_price']).ljust(8)} |")

            print("+----+----------------------+----------+----------+")

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

                choice = input("Half or Full? (h/f): ").strip().lower()

                if choice == "h":
                    price = selected_item["half_price"]
                    size = "Half"
                elif choice == "f":
                    price = selected_item["full_price"]
                    size = "Full"
                else:
                    print("Invalid choice!")
                    continue

                try:
                    qty = int(input("Enter Quantity: "))
                    if qty <= 0:
                        print("Quantity must be > 0")
                        continue
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

                print(f"{selected_item['name']} ({size}) x{qty} added → ₹{item_total}")

            if not order_items:
                print("\nNo order created!")
                return

            # -------- SUMMARY --------
            print("\n" + "=" * 60)
            print(" " * 20 + "ORDER SUMMARY")
            print("=" * 60)

            print("+----+----------------------+--------+-----+--------+")
            print("| ID | Item Name            | Size   | Qty | Total  |")
            print("+----+----------------------+--------+-----+--------+")

            for item in order_items:
                print(f"| {str(item['item_id']).ljust(2)} "
                      f"| {item['name'].ljust(20)} "
                      f"| {item['size'].ljust(6)} "
                      f"| {str(item['quantity']).ljust(3)} "
                      f"| ₹{str(item['total']).ljust(6)} |")

            print("+----+----------------------+--------+-----+--------+")
            print(f"\nGrand Total: ₹{total}")

            order_id = max([o.get("order_id", 0) for o in orders], default=0) + 1

            order_data = {
                "order_id": order_id,
                "staff": staff_name,
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "items": order_items,
                "total": total,
                "status": "Pending",
                "payment_method": None,
                "payment_time": None
            }

            orders.append(order_data)
            self.data.write(self.order_file, orders)

            report.append(order_data)
            self.data.write(self.report_file, report)

            print("\n" + "=" * 60)
            print("ORDER CREATED SUCCESSFULLY!")
            print(f"Order ID : {order_id}")
            print(f"Status   : Pending")
            print("=" * 60)

            return order_data

        except Exception as e:
            self.logger.log_error(f"CreateOrder Error: {str(e)}")
            print("Error creating order.")