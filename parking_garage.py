class ParkingGarage():
    def __init__(self):
        self.tickets = [1,2,3,4,5,6,7,8,9,10]
        self.parking_spaces = [1,2,3,4,5,6,7,8,9,10]
        self.current_ticket = {}

    def taketicket(self):
        if self.tickets:
            print(f'Your ticket number is {self.tickets[0]}')
            self.current_ticket[self.tickets[0]] = 'unpaid'
            self.tickets.pop(0)
            self.parking_spaces.pop(0)
        else:
            print("Garage is full, Thank you!")


    def payforparking(self):
        spot = int(input("What is your ticket number? "))
        if self.current_ticket.get(spot) == 'unpaid':
            print("Your ticket has been paid, you have 15 minutes to leave. Thank you!")
            self.current_ticket[spot] == 'paid'
            self.parking_spaces.append(spot)

    def leavegarage(self):
        vacant = int(input("What is your ticket number? "))
        if vacant not in self.current_ticket:
            print("Invalid ticket number.")
        elif self.current_ticket[vacant] == 'paid':
            print("Thank you, have a nice day!")
            self.tickets.append(vacant)
            del self.current_ticket[vacant]
        elif self.current_ticket[vacant] == 'unpaid':
            print("You must pay your ticket before leaving.")

    def garage(self):
        while True:
            response = input('What would you like to do? \n(T)Take Ticket, (P)Pay for Ticket, (L)Leave Garage, (Q)Quit >  ')
            if response.lower().strip() == 'q':
                print("Thank you for coming, we look forward to your business.")
                break
            elif response.lower().strip() == 't':
                ParkingGarage.taketicket(self)
            elif response.lower().strip() == 'p':
                ParkingGarage.payforparking(self)
            elif response.lower().strip() == 'l':
                ParkingGarage.leavegarage(self)

run = ParkingGarage()
run.garage()