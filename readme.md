# Turf Booking System

This Python program simulates a simple turf booking system, allowing an administrator to manage turf slots and a user to view and book available slots.

## Features

- **Admin:**
  - Add new turf slots with name, date, and time.
  - Remove existing turf slots.
  - View all available turf slots.
- **User:**
  - View available turf slots.
  - Book a turf slot.

## Classes

- **Turf:** Represents a single turf slot with attributes like ID, name, date, time, and availability.
- **Booking:** Represents a user's booking of a turf slot.
- **Admin:** Manages turf slots (adding, removing, viewing).
- **User:** Represents a user who can view and book turf slots.

## Usage

1.  **Run the program:** Execute the Python script.
2.  **Main Menu:** The program presents a main menu with options:
    -   "1. Admin Menu"
    -   "2. User Menu"
    -   "3. Exit"
3.  **Admin Menu:**
    -   "1. Add Turf"
    -   "2. Remove Turf"
    -   "3. View All Turfs"
4.  **User Menu:**
    -   "1. View Available Turfs"
    -   "2. Book Turf"

## Example Usage

**Admin:**

-   Select "1. Admin Menu".
-   Select "1. Add Turf".
-   Enter turf details (name, date, time).
-   Select "3. View All Turfs" to see the added turf slots.
-   Select "2. Remove Turf" and enter the turf ID to remove.

**User:**

-   Select "2. User Menu".
-   Select "1. View Available Turfs" to see the available slots.
-   Select "2. Book Turf" and enter the turf ID to book.

## Code Structure

-   **`Turf` class:**
    -   `__init__(self, id, name, date, time, available=True)`: Initializes a turf slot.
    -   `__str__(self)`: Returns a string representation of the turf slot.
-   **`Booking` class:**
    -   `__init__(self, user_name, turf, date, time)`: Initializes a booking.
    -   `__str__(self)`: Returns a string representation of the booking.
-   **`Admin` class:**
    -   `__init__(self)`: Initializes the admin with an empty list of turfs.
    -   `add_turf(self, name, date, time)`: Adds a new turf slot.
    -   `remove_turf(self, turf_id)`: Removes a turf slot by ID.
    -   `view_all_turfs(self)`: Displays all turf slots.
-   **`User` class:**
    -   `__init__(self, name)`: Initializes a user.
    -   `view_available_turfs(self, admin)`: Displays available turf slots.
    -   `book_turf(self, admin, turf_id)`: Books a turf slot.
-   **`main()` function:**
    -   Creates admin and user objects.
    -   Presents the main menu and handles user input.
    -   Calls the appropriate functions based on user choice.

## Dependencies

-   No external dependencies are required.

## Contributing

-   Feel free to contribute to this project by suggesting improvements or adding new features.

## License

-   This project is licensed under the [MIT License](LICENSE).