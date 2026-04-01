from app.database.data import data
from app.logs.logger import Logger

class DeleteOrder:

    def __init__(self):
        self.data = data()
        self.file = "app/database/orders.json"
        self.logger = Logger()  

    def delete(self):
        try:
            orders = self.data.read(self.file) or []

            if not orders:
                print("No orders found!")
                return

            try:
                order_id = int(input("Enter Order ID to delete: "))
            except ValueError:
                print("Invalid Order ID")
                return

            new_orders = []
            found = False

            for order in orders:
                if order.get("order_id") == order_id:
                    found = True
                    continue
                new_orders.append(order)

            if found:
                self.data.write(self.file, new_orders)
                print("Order Deleted Successfully!")
            else:
                print("Order ID not found!")

        except Exception as e:
            self.logger.log_error(f"DeleteOrder.delete Error: {str(e)}")
            print("Error deleting order. Check log for details.")