from app.database.data import data
from app.logs.logger import Logger  

class UpdateBooking:

    def __init__(self):
        self.data = data()
        self.file = "app/database/bookings.json"
        self.logger = Logger() 

    def update(self):
        try:
            bookings = self.data.read(self.file) or []

            if not bookings:
                print("No bookings found!")
                return

            try:
                booking_id = int(input("Enter Booking ID to update: "))
            except ValueError:
                print("Invalid Booking ID")
                return

            for booking in bookings:
                if booking.get("booking_id") == booking_id:

                    print("\nCurrent Booking Details")
                    print(booking)

                    # 👤 Customer Name
                    new_name = input("Enter New Customer Name: ").strip()
                    if new_name:
                        booking["customer_name"] = new_name

                    # 📱 Phone Validation (exact 10 digits)
                    while True:
                        new_phone = input("Enter New Phone: ").strip()
                        if not new_phone:
                            break
                        elif new_phone.isdigit() and len(new_phone) == 10:
                            booking["phone"] = new_phone
                            break
                        else:
                            print("Invalid phone! Must be exactly 10 digits.")

                    # 🍽 Table Validation (1–50)
                    while True:
                        new_table = input("Enter New Table No (1-50): ").strip()

                        if not new_table:
                            break

                        elif new_table.isdigit():
                            new_table = int(new_table)

                            if 1 <= new_table <= 50:

                                # check if already booked by another booking
                                if any(
                                    b.get("table_no") == new_table
                                    and b.get("booking_id") != booking_id
                                    for b in bookings
                                ):
                                    print(f"Table No {new_table} is already booked!")
                                else:
                                    booking["table_no"] = new_table
                                    break
                            else:
                                print("Invalid table! Enter between 1 and 50.")
                        else:
                            print("Please enter numbers only.")

                    # 👥 Persons Validation
                    while True:
                        new_persons = input("Enter New No. of Persons: ").strip()

                        if not new_persons:
                            break

                        elif new_persons.isdigit() and int(new_persons) > 0:
                            booking["persons"] = int(new_persons)
                            break
                        else:
                            print("Invalid number! Must be positive.")

                    self.data.write(self.file, bookings)
                    print("✅ Booking Updated Successfully!")
                    return

            print("Booking ID not found!")

        except Exception as e:
            self.logger.log_error(f"UpdateBooking Error: {str(e)}")
            print("Error:", e)