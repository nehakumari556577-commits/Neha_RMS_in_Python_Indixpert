from app.database.data import data
from app.logs.logger import Logger

class MonthlyReport:

    def __init__(self):
        self.data = data()
        self.file = "app/database/report.json"
        self.logger = Logger()  

    def monthly_report(self):
        try:
            orders = self.data.read(self.file) or []

            if not isinstance(orders, list):
                print("Invalid report data format")
                return

            if not orders:
                print("\nNo orders available for report")
                return

            month = input("Enter Month (YYYY-MM): ").strip()

            if len(month) != 7 or month[4] != "-":
                print("Invalid month format. Use YYYY-MM")
                return

            total_sales = 0
            total_orders = 0

            for order in orders:
                order_time = order.get("time", "")
                if order_time.startswith(month):
                    total_orders += 1
                    total = order.get("total", 0)
                    if isinstance(total, (int, float)):
                        total_sales += total

            print("\n" + "="*50)
            print("        MONTHLY REPORT")
            print("="*50)
            print(f"Month        : {month}")
            print(f"Total Orders : {total_orders}")
            print(f"Total Sales  : ₹{total_sales}")
            print("="*50)

        except Exception as e:
            self.logger.log_error(f"MonthlyReport.monthly_report Error: {str(e)}")
            print("Error generating monthly report. Check logs for details.")