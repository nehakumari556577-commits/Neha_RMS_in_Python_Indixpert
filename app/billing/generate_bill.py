from app.database.data import data
from datetime import datetime
from app.logs.logger import Logger 

class GenerateBill:

    def __init__(self):
        self.data = data()
        self.order_file = "app/database/orders.json"
        self.logger = Logger()  

    def generate(self):
        try:
            orders = self.data.read(self.order_file) or []

            if not orders:
                print("No orders found!")
                return

            print("\n===== GENERATE BILL =====")

            try:
                order_id = int(input("Enter Order ID: "))
            except ValueError:
                print("Invalid Order ID")
                return

            selected_order = None

            for order in orders:
                if order.get("order_id") == order_id:
                    selected_order = order
                    break

            if not selected_order:
                print("Order not found!")
                return

            if selected_order.get("status") == "Paid":
                print(f"Order {order_id} is already paid via {selected_order.get('payment_method', 'N/A')}")
                return

            subtotal = selected_order.get("total", 0)
            gst = subtotal * 0.05
            grand_total = subtotal + gst

            print("\n===== PAYMENT =====")
            print("1 Cash")
            print("2 UPI")
            print("3 Card")

            choice = input("Select Payment Mode: ").strip()

            if choice == "1":
                payment_mode = "Cash"
            elif choice == "2":
                payment_mode = "UPI"
            elif choice == "3":
                payment_mode = "Card"
            else:
                payment_mode = "Cash"


            selected_order["status"] = "Paid"
            selected_order["payment_method"] = payment_mode
            selected_order["payment_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            self.data.write(self.order_file, orders)


            print("\n=========== BILL ===========")
            print(f"Order ID : {selected_order['order_id']}")
            print(f"Staff    : {selected_order.get('staff', 'N/A')}")
            print(f"Date     : {datetime.now().strftime('%Y-%m-%d %H:%M')}")
            print("-" * 30)

            for item in selected_order.get("items", []):
                print(f"{item['name']} ({item['size']}) x{item['quantity']} = ₹{item['total']}")

            print("-" * 30)
            print(f"Subtotal     : ₹{subtotal}")
            print(f"GST (5%)     : ₹{round(gst, 2)}")
            print(f"Grand Total  : ₹{round(grand_total, 2)}")
            print(f"Payment Mode : {payment_mode}")
            print("=" * 30)

            print("\nBill Generated Successfully!")

        except Exception as e:
            self.logger.log_error(f"GenerateBill Error: {str(e)}")
            print("Error:", e)