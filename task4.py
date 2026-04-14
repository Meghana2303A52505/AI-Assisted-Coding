from datetime import datetime

class Booking:
    def __init__(self, ticket_id, passenger_name, train_number, seat_number, travel_date):
        self.ticket_id = ticket_id
        self.passenger_name = passenger_name
        self.train_number = train_number
        self.seat_number = seat_number
        self.travel_date = datetime.strptime(travel_date, "%Y-%m-%d")

    def __repr__(self):
        return (f"Booking(ticket_id={self.ticket_id}, passenger_name={self.passenger_name}, "
                f"train_number={self.train_number}, seat_number={self.seat_number}, "
                f"travel_date={self.travel_date.strftime('%Y-%m-%d')})")

class RailwayReservationSystem:
    def __init__(self):
        self.bookings = []
        self.ticket_index = {}

    def add_booking(self, booking):
        self.bookings.append(booking)
        self.ticket_index[booking.ticket_id] = booking

    # Efficient search: Hash table (dictionary) lookup for ticket ID (O(1) time)
    def search_ticket(self, ticket_id):
        return self.ticket_index.get(ticket_id, None)

    # Efficient sort: Python's built-in sort (Timsort, O(n log n)), stable and fast
    def sort_bookings_by_date(self):
        self.bookings.sort(key=lambda b: b.travel_date)

    def sort_bookings_by_seat(self):
        self.bookings.sort(key=lambda b: b.seat_number)

# Example usage
if __name__ == "__main__":
    system = RailwayReservationSystem()
    system.add_booking(Booking("T001", "Alice", "12345", 12, "2024-07-01"))
    system.add_booking(Booking("T002", "Bob", "12345", 5, "2024-06-30"))
    system.add_booking(Booking("T003", "Charlie", "54321", 8, "2024-07-02"))

    # Search
    print("Search T002:", system.search_ticket("T002"))

    # Sort by date
    system.sort_bookings_by_date()
    print("Sorted by date:", system.bookings)

    # Sort by seat number
    system.sort_bookings_by_seat()
    print("Sorted by seat:", system.bookings)