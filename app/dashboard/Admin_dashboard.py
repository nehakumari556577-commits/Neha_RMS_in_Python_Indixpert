# app/dashboard/admin_dashboard.py

from app.database.data import data
from app.menu.add_item import AddMenuItem
from app.menu.view_menu import ViewMenu
from app.menu.update_item import UpdateMenuItem
from app.menu.delete_item import DeleteMenuItem

from app.order.create_order import CreateOrder
from app.order.view_orders import ViewOrder
from app.order.update_order import UpdateOrder
from app.order.delete_order import DeleteOrder

from app.booking.create_booking import CreateBooking
from app.booking.view_booking import ViewBooking
from app.booking.update_booking import UpdateBooking
from app.booking.cancel_booking import CancelBooking

from app.report.today_report import TodayReport
from app.report.total_sales import TotalSales
from app.report.most_sold_item import MostSoldItem
from app.report.monthly_report import MonthlyReport
from app.report.top_customers import TopCustomers

from app.logs.logger import Logger


class AdminDashboard:

    def __init__(self, user):
        self.user = user
        self.data = data()
        self.logger = Logger()  

        self.add_item = AddMenuItem()
        self.view_menu = ViewMenu()
        self.update_item = UpdateMenuItem()
        self.delete_item = DeleteMenuItem()

    
        self.create_order = CreateOrder()
        self.order_view = ViewOrder()
        self.update_order_obj = UpdateOrder()
        self.delete_order_obj = DeleteOrder()

    
        self.create_booking = CreateBooking()
        self.booking_view = ViewBooking()
        self.update_booking_obj = UpdateBooking()
        self.cancel_booking_obj = CancelBooking()


        self.today = TodayReport()
        self.sales = TotalSales()
        self.most = MostSoldItem()
        self.month = MonthlyReport()
        self.customer = TopCustomers()


    def start(self):
        while True:
            try:
                print("\n" + "=" * 70)
                print("ADMIN DASHBOARD".center(70))
                print("=" * 70)

                print(f"User : {self.user['name']}")
                print("-" * 70)

                print("1. Manage Menu")
                print("2. Manage Orders")
                print("3. Manage Bookings")
                print("4. Reports")
                print("5. Logout")
                print("-" * 70)

                choice = input("Enter choice: ")

                if not choice.isdigit():
                    print("Invalid input.")
                    continue

                choice = int(choice)

                if choice == 1:
                    self.menu_manage()

                elif choice == 2:
                    self.order_manage()

                elif choice == 3:
                    self.booking_manage()

                elif choice == 4:
                    self.report_manage()

                elif choice == 5:
                    print("Logging out...")
                    break

                else:
                    print("Invalid choice.")

            except Exception as e:
                self.logger.log_error(f"AdminDashboard Error: {str(e)}")
                print("Error occurred. Check log.")

    def menu_manage(self):
        while True:
            try:
                print("\n===== MENU MANAGEMENT =====")
                print("1. View Menu")
                print("2. Add Item")
                print("3. Update Item")
                print("4. Delete Item")
                print("5. Back")

                choice = input("Enter choice: ")

                if choice == "1":
                    self.view_menu.show_menu()

                elif choice == "2":
                    self.add_item.add_item()

                elif choice == "3":
                    self.update_item.update_item()

                elif choice == "4":
                    self.delete_item.delete_item()

                elif choice == "5":
                    break

                else:
                    print("Invalid choice.")

            except Exception as e:
                self.logger.log_error(f"Menu Management Error: {str(e)}")
                print("Error occurred. Check log.")


    def order_manage(self):
        while True:
            try:
                print("\n===== ORDER MANAGEMENT =====")
                print("1. Create Order")
                print("2. View Orders")
                print("3. Update Order Status")
                print("4. Delete Order")
                print("5. Back")

                choice = input("Enter choice: ")

                if choice == "1":
                    self.create_order.create(self.user["name"])

                elif choice == "2":
                    self.order_view.view_orders()

                elif choice == "3":
                    self.update_order_obj.update()  

                elif choice == "4":
                    self.delete_order_obj.delete()  

                elif choice == "5":
                    break

                else:
                    print("Invalid choice.")

            except Exception as e:
                self.logger.log_error(f"Order Management Error: {str(e)}")
                print("Error occurred. Check log.")


    def booking_manage(self):
        while True:
            try:
                print("\n===== BOOKING MANAGEMENT =====")
                print("1. Create Booking")
                print("2. View Bookings")
                print("3. Update Booking")
                print("4. Cancel Booking")
                print("5. Back")

                choice = input("Enter choice: ")

                if choice == "1":
                    self.create_booking.create()

                elif choice == "2":
                    self.booking_view.view_bookings()

                elif choice == "3":
                    self.update_booking_obj.update() 

                elif choice == "4":
                    self.cancel_booking_obj.cancel()  

                elif choice == "5":
                    break

                else:
                    print("Invalid choice.")

            except Exception as e:
                self.logger.log_error(f"Booking Management Error: {str(e)}")
                print("Error occurred. Check log.")


    def report_manage(self):
        while True:
            try:
                print("\n===== REPORTS =====")
                print("1. Today Report")
                print("2. Total Sales")
                print("3. Most Sold Item")
                print("4. Monthly Report")
                print("5. Top Customers")
                print("6. Back")

                choice = input("Enter choice: ")

                if choice == "1":
                    self.today.today_report()

                elif choice == "2":
                    self.sales.total_sales()

                elif choice == "3":
                    self.most.most_sold_item()

                elif choice == "4":
                    self.month.monthly_report()

                elif choice == "5":
                    self.customer.top_customers()

                elif choice == "6":
                    break

                else:
                    print("Invalid choice.")

            except Exception as e:
                self.logger.log_error(f"Report Management Error: {str(e)}")
                print("Error occurred. Check log.")