from app.database.data import data
from app.logs.logger import Logger

class MostSoldItem:

    def __init__(self):
        self.data = data()
        self.file = "app/database/report.json"
        self.logger = Logger() 

    def most_sold_item(self):
        try:
            orders = self.data.read(self.file) or []
            item_count = {}

            for order in orders:
                for item in order.get("items", []):
                    name = item.get("name")
                    qty = item.get("quantity", 0)

                    if name:
                        item_count[name] = item_count.get(name, 0) + qty

            if not item_count:
                print("No data found for most sold item")
                return

            most_item = max(item_count, key=item_count.get)

            print("\n" + "="*50)
            print("        MOST SOLD ITEM")
            print("="*50)
            print(f"Item Name : {most_item}")
            print(f"Quantity  : {item_count[most_item]}")
            print("="*50)

        except Exception as e:
            self.logger.log_error(f"MostSoldItem.most_sold_item Error: {str(e)}")
            print("Error generating most sold item report. Check logs for details.")