from app.database.data import data
from app.logs.logger import Logger  

class ViewBooking:

    def __init__(self):
        self.data = data()
        self.file = "app/database/bookings.json"
        self.logger = Logger() 

    def view_bookings(self):
        try:
            bookings = self.data.read(self.file) or []

            if not isinstance(bookings, list):
                print("Invalid booking data format")
                return

            if not bookings:
                print("\nNo bookings found")
                return

            print("\n" + "=" * 85)
            print("+----+----------------------+-------------+----------+---------+---------------------+")
            print("| ID | Name                 | Phone       | Table No | Persons | Time                |")
            print("+----+----------------------+-------------+----------+---------+---------------------+")

            for b in bookings:
                booking_id = b.get("booking_id", "N/A")
                name = str(b.get("customer_name", "N/A"))[:20]
                phone = str(b.get("phone", "N/A"))[:11]
                table_no = b.get("table_no", "N/A")
                persons = b.get("persons", "N/A")
                time = b.get("time", "N/A")

                print(f"| {str(booking_id):<2} "
                      f"| {name:<20} "
                      f"| {phone:<11} "
                      f"| {str(table_no):<8} "
                      f"| {str(persons):<7} "
                      f"| {time:<19} |")

            print("+----+----------------------+-------------+----------+---------+---------------------+")
            print("=" * 85)

        except Exception as e:
            self.logger.log_error(f"ViewBooking Error: {str(e)}")
            print("Error:", e)