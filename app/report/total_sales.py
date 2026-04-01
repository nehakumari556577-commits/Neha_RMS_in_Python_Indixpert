from app.database.data import data
from app.logs.logger import Logger

class TotalSales:

    def __init__(self):
        self.data = data()
        self.file = "app/database/report.json"
        self.logger = Logger() 

    def total_sales(self):
        try:
            orders = self.data.read(self.file) or []

            if not isinstance(orders, list):
                print("Invalid report data format")
                return

            if not orders:
                print("\nNo orders available for sales report")
                return

            total = sum(order.get("total", 0) for order in orders)

            print("\n" + "="*50)
            print("          TOTAL SALES")
            print("="*50)
            print(f"Total Revenue : ₹{total}")
            print("="*50)

        except Exception as e:
            self.logger.log_error(f"TotalSales.total_sales Error: {str(e)}")
            print("Error generating total sales report. Check logs for details.")