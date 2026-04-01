from app.database.data import data
from app.logs.logger import Logger

class UpdateOrder:

    def __init__(self):
        self.data = data()
        self.file = "app/database/orders.json"
        self.logger = Logger() 

    def update(self):
        try:
            orders = self.data.read(self.file) or []

            if not orders:
                print("No orders found!")
                return

            try:
                order_id = int(input("Enter Order ID to update: "))
            except ValueError:
                print("Invalid Order ID")
                return

            for order in orders:
                if order.get("order_id") == order_id:

                    print("\nCurrent Order Details")
                    print(order)

                    print("\nSelect New Status")
                    print("1. Pending")
                    print("2. Preparing")
                    print("3. Completed")
                    print("4. Cancelled")

                    choice = input("Enter choice: ").strip()

                    status_map = {
                        "1": "Pending",
                        "2": "Preparing",
                        "3": "Completed",
                        "4": "Cancelled"
                    }

                    if choice in status_map:
                        order["status"] = status_map[choice]
                    else:
                        print("Invalid choice!")
                        return

                    self.data.write(self.file, orders)
                    print("Order Status Updated Successfully!")
                    return

            print("Order ID not found!")

        except Exception as e:
            self.logger.log_error(f"UpdateOrder.update Error: {str(e)}")
            print("Error updating order. Check log for details.")