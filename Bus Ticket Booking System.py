print("---- Bus Ticket Booking System ----")
total_seats = 50

while True:
    print("\n---- Bus Menu ----")
    print("1. Check Available Seats")
    print("2. Book Ticket")
    print("3. Cancel Ticket")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Available Seats:", total_seats)

    elif choice == 2:
        tickets = int(input("Enter number of tickets to book: "))
        if tickets <= total_seats:
            total_seats = total_seats - tickets
            print("Ticket booked successfully")
        else:
            print("Not enough seats available")

    elif choice == 3:
        tickets = int(input("Enter number of tickets to cancel: "))
        total_seats = total_seats + tickets
        print("Ticket cancelled successfully")

    elif choice == 4:
        print("Thank you for using Bus Ticket Booking System")
        break

    else:
        print("Invalid choice, please try again")
