from app.database.data import data
from datetime import datetime
from app.logs.logger import Logger 

class CreateBooking:

    def __init__(self):
        self.data = data()
        self.file = "app/database/bookings.json"
        self.logger = Logger()  

    def create(self):
        try:
            bookings = self.data.read(self.file) or []

            print("\n===== TABLE BOOKING =====")

            name = input("Enter Customer Name: ").strip()
            if not name:
                print("Customer name is required!")
                return

            while True:
                phone = input("Enter Phone: ").strip()
                if phone.isdigit() and len(phone) == 10:
                    break
                else:
                    print("Invalid phone number! Enter exactly 10 digits.")


            while True:
                table_no = input("Enter Table No (1-50): ").strip()

                if table_no.isdigit():
                    table_no = int(table_no)

                    if 1 <= table_no <= 50:

        
                        if any(b.get("table_no") == table_no for b in bookings):
                            print(f"Table No {table_no} is already booked!")
                        else:
                            break
                    else:
                        print("Invalid Table Number! Please enter between 1 and 50.")
                else:
                    print("Please enter numbers only.")

            while True:
                persons = input("Enter Number of Persons: ").strip()
                if persons.isdigit() and int(persons) > 0:
                    persons = int(persons)
                    break
                else:
                    print("Invalid number of persons! Must be a positive number.")

            booking_id = max(
                [b.get("booking_id", 0) for b in bookings],
                default=0
            ) + 1

            booking_data = {
                "booking_id": booking_id,
                "customer_name": name,
                "phone": phone,
                "table_no": table_no,
                "persons": persons,
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            bookings.append(booking_data)
            self.data.write(self.file, bookings)

            print("\nBooking Created Successfully!")
            print(f"Booking ID : {booking_id}")
            print(f"Name       : {name}")
            print(f"Table No   : {table_no}")
            print(f"Persons    : {persons}")
            print(f"Time       : {booking_data['time']}")

            return booking_data

        except Exception as e:
            self.logger.log_error(f"CreateBooking Error: {str(e)}")
            print("Error:", e)