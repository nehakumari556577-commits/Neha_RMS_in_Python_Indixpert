from app.database.data import data
from app.logs.logger import Logger

class ViewOrder:

    def __init__(self):
        self.data = data()
        self.file = "app/database/orders.json"
        self.logger = Logger()  

    def view_orders(self):
        try:
            orders = self.data.read(self.file) or []

            if not isinstance(orders, list):
                print("Invalid order data format")
                return

            if not orders:
                print("\nNo orders found")
                return

            print("\n" + "="*80)
            print("                 ORDER DETAILS")
            print("="*80)

            for o in orders:
                if "order_id" not in o:
                    continue  

                print("\n" + "-"*80)
                print(f"Order ID       : {o.get('order_id', 'N/A')}")
                print(f"Staff          : {o.get('staff', 'N/A')}")
                print(f"Status         : {o.get('status', 'N/A')}")
                print(f"Payment Mode   : {o.get('payment_method', 'N/A')}")
                print(f"Order Time     : {o.get('time', 'N/A')}")
                print(f"Payment Time   : {o.get('payment_time', 'N/A')}")

                print("\nItems:")
                print("-" * 80)

                for item in o.get("items", []):
                    name = item.get("name", "N/A")
                    price = item.get("price", 0)
                    qty = item.get("quantity", 0)
                    size = item.get("size", "N/A")
                    total_item = item.get("total", price * qty)
                    print(f"{name:<25} {size:<6} ₹{price:<8} x {qty} = ₹{total_item}")

                print("-" * 80)
                print(f"Total Amount   : ₹{o.get('total', 0)}")
                print("-" * 80)

            print("\n" + "="*80)

        except Exception as e:
            self.logger.log_error(f"ViewOrder.view_orders Error: {str(e)}")
            print("Error displaying orders. Check log for details.")