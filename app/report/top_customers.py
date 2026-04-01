from app.database.data import data
from app.logs.logger import Logger

class TopCustomers:

    def __init__(self):
        self.data = data()
        self.file = "app/database/report.json"
        self.logger = Logger()  

    def top_customers(self, top_n=5):
        try:
            orders = self.data.read(self.file) or []

            if not isinstance(orders, list):
                print("Invalid report data format")
                return

            customer_data = {}
            for order in orders:
        
                name = order.get("staff") or "Unknown"
                customer_data[name] = customer_data.get(name, 0) + order.get("total", 0)

            if not customer_data:
                print("No data found")
                return

            sorted_customers = sorted(customer_data.items(), key=lambda x: x[1], reverse=True)

            print("\n" + "="*60)
            print("          TOP CUSTOMERS")
            print("="*60)

            for idx, (cust, total) in enumerate(sorted_customers[:top_n], start=1):
                print(f"{idx}. {cust:<20} - Total Spend: ₹{total}")

            print("="*60)

        except Exception as e:
            self.logger.log_error(f"TopCustomers.top_customers Error: {str(e)}")
            print("Error generating top customers report. Check logs for details.")