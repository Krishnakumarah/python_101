class BusTicketSystem:
    def __init__(self, total_seats):
        self.total_seats = total_seats
        self.available_seats = total_seats

    def book_seat(self):
        if self.available_seats > 0:
            self.available_seats -= 1
            print(f"Seat booked. {self.available_seats} seats remaining.")
        else:
            print("All seats are booked.")

def main():
    bus = BusTicketSystem(8)
    while bus.available_seats > 0:
        book_now = input("Press 'b' to book a seat or any other key to exit: ").lower()
        if book_now == 'b':
            bus.book_seat()
        else:
            break
    if bus.available_seats == 0:
        print("All seats are booked.")

if __name__ == "__main__":
    main()
