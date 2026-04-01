from app.database.data import data
from datetime import datetime
from app.logs.logger import Logger

class TodayReport:

    def __init__(self):
        self.data = data()
        self.file = "app/database/report.json"
        self.logger = Logger()  

    def today_report(self):
        try:
            orders = self.data.read(self.file) or []
            today = datetime.now().strftime("%Y-%m-%d")

            if not isinstance(orders, list):
                print("Invalid report data format")
                return

            total_orders = 0
            total_sales = 0

            print("\n" + "="*50)
            print("          TODAY REPORT")
            print("="*50)

            for order in orders:
                order_time = order.get("time", "")
                if order_time.startswith(today):
                    total_orders += 1
                    total_sales += order.get("total", 0)

            print(f"Total Orders : {total_orders}")
            print(f"Total Sales  : ₹{total_sales}")
            print("="*50)

        except Exception as e:
            self.logger.log_error(f"TodayReport.today_report Error: {str(e)}")
            print("Error generating today's report. Check logs for details.")