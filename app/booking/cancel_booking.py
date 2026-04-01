from app.database.data import data
from app.logs.logger import Logger 

class CancelBooking:

    def __init__(self):
        self.data = data()
        self.file = "app/database/bookings.json"
        self.logger = Logger() 

    def cancel(self):
        try:
            bookings = self.data.read(self.file) or []

            if not bookings:
                print("No bookings found!")
                return

            try:
                booking_id = int(input("Enter Booking ID to cancel: "))
            except ValueError:
                print("Invalid Booking ID")
                return

            new_bookings = []
            found = False

            for booking in bookings:
                if booking.get("booking_id") == booking_id:
                    found = True
                    continue 
                new_bookings.append(booking)

            if found:
                self.data.write(self.file, new_bookings)
                print("Booking Cancelled Successfully!")
            else:
                print("Booking ID not found!")

        except Exception as e:
            self.logger.log_error(f"CancelBooking Error: {str(e)}")
            print("Error:", e)