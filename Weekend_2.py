# Class Methods
# Your Parking Garage class should implement the following methods:

# - take_ticket:
#   - Decrease the number of available tickets and parking spaces by 1.
# - pay_for_parking:
#   - Show an input prompt asking for the payment amount.
#   - If the payment variable is not empty, display a message that the ticket has been paid and they have 15 minutes to leave.
#   - Update the `current_ticket` dictionary, setting the key "paid" to True.
 
# - leave_garage:
#   - If the ticket has been paid, display a "Thank You, have a nice day" message.
#   - If not, prompt for payment.
#   - Once paid, update the parking spaces and tickets lists to increase by 1.

# Attributes
# You will need the following attributes:
# - `tickets` (list)
# - `parking_spaces` (list)
# - `current_ticket` (dictionary)

# Environment & Accountability
# Use VSCode for this project and start with the files linked below. Each person should document the portion of the project they contributed to within the Python file and the README.

# Learning Objectives
# By the end of this project, each group/student should be able to:
# - Demonstrate proficiency in using Git and GitHub for collaboration.
# - Understand the concept of classes and object-oriented programming.
# - Create class methods and understand their utility.
# - Demonstrate how to instantiate classes.

# instance = object   class = values, structure.
# Final Steps
# Upon project completion, commit the final changes, synchronize all pull requests, and submit your GitHub links. The code should be identical across all members of the team.

tickets = ()

parking_spaces = ()

current_ticket = {}

class ParkingGarage:
    def __init__(self, total_tickets=100,total_spaces=100):
        self.ticket = [i for i in range(1, total_tickets +1)]
        self.parking_spaces = [i for i in range(1, total_spaces +1)]
        self.current_ticket = {}         
        
def Take_ticket(self):
    if len(self.tickets) >0 and len(self.parking_spaces) > 0:
        ticket = self.tickets.pop(0)
        space = self.parking_spaces.pop(0)
        print(f'Your ticket number is {ticket} and your parking space is {space} ')
    else:
        print("Sorry, the garage is full.")

def Pay_for_parking(self):
        ticket = int(input("Enter your ticket number: "))
        if ticket in self.current_ticket:
            if not self.current_ticket[ticket]['paid']:
                payment = input("Please enter payment amount: ")
                if payment:
                    self.current_ticket[ticket]['paid'] = True
                else:
                    print("Your ticket has been paid.  You have 15 minutes to leave, or we will have to use excessive force")
            else:
                 print ("The ticket has been paid. ")
        else:
                 print("Wrong ticket number.")                
       
def Leave_garage(self):
     ticket = int(input("We need your ticket number to exit: "))

     if ticket in self.current_ticket:
          if self.current_ticket[ticket]['paid']:
               print("Thank you, have a wonderful day. ")
               del self.current_ticket[ticket]
               self.tickets.append(ticket)
               self.parking_spaces.append(ticket)
     else:
          print("Wrong ticket number! I'll wait.....")