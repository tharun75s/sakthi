class Turf:
    def __init__(self, id, name, date, time, available=True):
        self.id = id
        self.name = name
        self.date = date
        self.time = time
        self.available = available

    def __str__(self):
        return f"ID: {self.id}, Turf: {self.name}, Date: {self.date}, Time: {self.time}, Available: {self.available}"
class Booking:
    def __init__(self, user_name, turf, date, time):
        self.user_name = user_name
        self.turf = turf
        self.date = date
        self.time = time

    def __str__(self):
        return f"Booking: {self.user_name} booked {self.turf.name} on {self.date} at {self.time}"
class Admin:
    def __init__(self):
        self.turfs = []

    def add_turf(self, name, date, time):
        turf_id = len(self.turfs) + 1
        turf = Turf(turf_id, name, date, time)
        self.turfs.append(turf)
        print(f"Turf slot added: {turf}")

    def remove_turf(self, turf_id):
        for turf in self.turfs:
            if turf.id == turf_id:
                self.turfs.remove(turf)
                print(f"Turf slot removed: {turf}")
                return
        print("Turf ID not found!")

    def view_all_turfs(self):
        if not self.turfs:
            print("No turfs available.")
        for turf in self.turfs:
            print(turf)
class User:
    def __init__(self, name):
        self.name = name
        self.bookings = []

    def view_available_turfs(self, admin):
        available_turfs = [turf for turf in admin.turfs if turf.available]
        if not available_turfs:
            print("No turfs available for booking.")
        for turf in available_turfs:
            print(turf)

    def book_turf(self, admin, turf_id):
        for turf in admin.turfs:
            if turf.id == turf_id and turf.available:
                booking = Booking(self.name, turf, turf.date, turf.time)
                self.bookings.append(booking)
                turf.available = False  # Mark the turf as booked
                print(f"Booking successful: {booking}")
                return
        print("Turf not available for booking.")
def main():
    admin = Admin()
    
    # Admin adds some turf slots
    admin.add_turf("Football Turf", "2025-03-20", "10:00 AM")
    admin.add_turf("Football Turf", "2025-03-20", "02:00 PM")
    admin.add_turf("Cricket Turf", "2025-03-21", "04:00 PM")
    admin.add_turf("Cricket Turf", "2025-03-21", "06:00 PM")
    
    user = User("John Doe")

    while True:
        print("\n--- Main Menu ---")
        print("1. Admin Menu")
        print("2. User Menu")
        print("3. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':  # Admin Menu 
            print("\n--- Admin Menu ---")
            print("1. Add Turf")
            print("2. Remove Turf")
            print("3. View All Turfs")
            admin_choice = input("Enter your choice: ")
            
            if admin_choice == '1':
                name = input("Enter Turf Name: ")
                date = input("Enter Turf Date (YYYY-MM-DD): ")
                time = input("Enter Turf Time (HH:MM AM/PM): ")
                admin.add_turf(name, date, time)
            elif admin_choice == '2':
                turf_id = int(input("Enter Turf ID to remove: "))
                admin.remove_turf(turf_id)
            elif admin_choice == '3':
                admin.view_all_turfs()
            else:
                print("Invalid choice. Returning to main menu.")
        
        elif choice == '2':  # User Menu
            print("\n--- User Menu ---")
            print("1. View Available Turfs")
            print("2. Book Turf")
            user_choice = input("Enter your choice: ")
            
            if user_choice == '1':
                user.view_available_turfs(admin)
            elif user_choice == '2':
                turf_id = int(input("Enter Turf ID to book: "))
                user.book_turf(admin, turf_id)
            else:
                print("Invalid choice. Returning to main menu.")
        
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
