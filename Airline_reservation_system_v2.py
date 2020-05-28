
# TASK!
# Airline Reservation System** - Create a reservation system which books airline seats.
# It charges various rates for particular sections of the plane.
# Example, first class is going to cost more than coach.
# Keep track of when rooms will be available and can be scheduled.
# PROGRAM CODE
import random
from IPython.display import clear_output
# Function which displays the plane layout with economy and first classes seats
# Economny class designed to be 36 seats, first class 12 seats
def display_seats(a, b, a_price, b_price):
    clear_output()
    economy_seats = 36 - a.count(' x')
    first_seats = 12 - b.count(' x ')
    print('               ===========           ')
    print('               \\'+'\\'+'        \\'+'\\')
    print('                \\'+'\\'+'        \\'+'\\')
    print('                 \\'+'\\'+'        \\'+'\\')
    print('                  \\'+'\\'+'        \\'+'\\')
    print('                   \\'+'\\'+'        \\'+'\\')
    print('                    \\'+'\\'+'        \\'+'\\')
    print('                     \\'+'\\'+'        \\'+'\\')
    print('==================================================================================')
    print('['+a[0]+' ] '+'['+a[1]+' ] '+'['+a[2]+' ] '+'['+a[3]+' ] '+'['+a[4]+' ] '+ \
          '['+a[5]+' ] '+'['+a[6]+' ] '+'['+a[7]+' ] '+'['+a[8]+' ] '+'|| '+'['+b[0]+ \
          ' ]  '+'['+b[1]+' ]  '+'['+b[2]+' ]  '+'\\'+'\\')
    print('['+a[9]+' ] '+'['+a[10]+' ] '+'['+a[11]+' ] '+'['+a[12]+' ] '+'['+a[13]+' ] '+ \
          '['+a[14]+' ] '+'['+a[15]+' ] '+'['+a[16]+' ] '+'['+a[17]+' ] '+'|| '+'['+b[3]+ \
          ' ]  '+'['+b[4]+' ]  '+'['+b[5]+' ]  '+' \\'+'\\')
    print('<-------------------ECONOMY CLASS---------------------><--------FIRST CLASS------->')
    print('['+a[18]+' ] '+'['+a[19]+' ] '+'['+a[20]+' ] '+'['+a[21]+' ] '+'['+a[22]+' ] '+ \
          '['+a[23]+' ] '+'['+a[24]+' ] '+'['+a[25]+' ] '+'['+a[26]+' ] '+'|| '+'['+b[6]+ \
          ' ]  '+'['+b[7]+' ]  '+'['+b[8]+' ]  '+' //')
    print('['+a[27]+' ] '+'['+a[28]+' ] '+'['+a[29]+' ] '+'['+a[30]+' ] '+'['+a[31]+' ] '+ \
          '['+a[32]+' ] '+'['+a[33]+' ] '+'['+a[34]+' ] '+'['+a[35]+' ] '+'|| '+'['+b[9]+ \
          ' ]  '+'['+b[10]+' ]  '+'['+b[11]+' ]  '+'//')
    print('==================================================================================')
    print('                     //'+ '        //')
    print('                    //'+ '        //' \
          '    =ECONOMY CLASS=          =FIRST CLASS=')
    print('                   //'+ '        //' \
          f'     Seats available: {economy_seats}      Seats available: {first_seats} ')     
    print('                  //'+ '        //' \
          f'      Seat price: {a_price}$          Seat price: {b_price}$ ')
    print('                 //'+ '        //')
    print('                //'+ '        //')
    print('               //'+ '        //')
    print('               ===========           ')
# Seats class which creates a list of economy seats with names and first class seats with names
class Seats():
    def __init__(self, seats, price):
        rows = ['A', 'B', 'C', 'D']
        self.seats = seats
        self.seats_plan = []
        self.price = price
        if self.seats > 12:
            for letter in rows:
                for number in range(1, 10):
                    self.seats_plan.append(str(number)+letter)
        else:
            for letter in rows:
                for number in range(10, 13):
                    self.seats_plan.append(str(number)+letter)
    def __str__(self):
        seats_string = ''
        i = 1
        for s in self.seats_plan:
            seats_string += i.__str__() + " - " + s.__str__() +'\n'
            i += 1
        return seats_string
    def rand_filling(self):
        rand_number = random.randint(0, len(self.seats_plan)-1)
        for numb in range(0, rand_number):
            if self.seats > 12:
                self.seats_plan[random.randint(0, len(self.seats_plan)-1)] = ' x'
            else:
                self.seats_plan[random.randint(0, len(self.seats_plan)-1)] = ' x '

# Class - budget which is showing amount of money in budget and have a method for transaction
class Budget():
    def __init__(self, budget):
        self.budget = budget
    def transaction(self, price):
        self.budget -= price
# Function for checking if there are available seats which can be reserved and purchased
def check_availability(economy, first):
    return economy.count(' x') == 36 and first.count(' x ') == 12
# Creating economy class 36 seats with seats names and setting price - 79 for one seat.
ECONOMY = Seats(36, 79)
# Creating first class 12 seats with seats names and setting price - 199 for one seat.
FIRST = Seats(12, 199)
# Creating randomly reserved plane seats.
ECONOMY.rand_filling()
FIRST.rand_filling()
# Setting budget
MYBUDGET = Budget(1000)
RESERVATIONS = ''
TOTAL_PURCHASES = 0
RUN_PROGRAM = True
# if the want to reserve a seat, then proceed with code
START = input('\nHello. Welcome to the SUPER AIRLINES.' \
              'Do you want to reserve e seat for your flight? YES / NO\n')
if START[0].lower() != 'y':
    RUN_PROGRAM = False
while RUN_PROGRAM:
    # checking if there are free spaces available
    if check_availability(ECONOMY.seats_plan, FIRST.seats_plan) == True:
        print('We sorry, there are no available seats.')
        break
    #displaying seats before reservation
    display_seats(ECONOMY.seats_plan, FIRST.seats_plan, ECONOMY.price, FIRST.price)
    ORDER = input("Please enter the number of the seat that you want to reserve!")
    #while seat is not already reserved, proceed with reservation code
    while (ORDER not in ECONOMY.seats_plan) and (ORDER not in FIRST.seats_plan):
        ORDER = input("The seat number is occupied or doesn't exist."+
                      " Please enter the correct number of the seat that you want to reserve!")
    else:
        if (ORDER in FIRST.seats_plan and MYBUDGET.budget < FIRST.price) or \
        (ORDER in ECONOMY.seats_plan and MYBUDGET.budget < ECONOMY.price):
            print("\nSorry, you don't have enough money")
            RUN_PROGRAM = False
        else:
            # checking in the seat is in the first class and if there is enough money in the budget
            if ORDER in FIRST.seats_plan:
                MYBUDGET.transaction(FIRST.price)
                SEAT_INDEX = FIRST.seats_plan.index(ORDER)
                NAME = input("Please enter the name of the passenger ")
                RESERVATIONS += str(FIRST.seats_plan[SEAT_INDEX])+"-"+ \
                                NAME+"-"+str(FIRST.price)+'$\n'
                #reserving a seat and changing it's number to 'x'
                #so that it would we visible in seats plan display
                TOTAL_PURCHASES += FIRST.price
                FIRST.seats_plan[SEAT_INDEX] = ' x '
            # the same code with the economy class
            elif ORDER in ECONOMY.seats_plan:
                MYBUDGET.transaction(ECONOMY.price)
                SEAT_INDEX = ECONOMY.seats_plan.index(ORDER)
                NAME = input("Please enter the name of the passenger ")
                RESERVATIONS += str(ECONOMY.seats_plan[SEAT_INDEX])+"-"+ \
                                NAME+"-"+str(ECONOMY.price)+'$\n'
                TOTAL_PURCHASES += ECONOMY.price
                ECONOMY.seats_plan[SEAT_INDEX] = ' x'
            # displaying seats after seat is reserved
            display_seats(ECONOMY.seats_plan, FIRST.seats_plan, ECONOMY.price, FIRST.price)
            print('\nThank you! Seat is reserved!')
            print(f'Current account balance: {MYBUDGET.budget}$')
            # asking if want another reservation
            REPEAT = input('Do you want to reserve another seat? YES / NO')
            if REPEAT[0].lower() == 'y':
                continue
            else:
                RUN_PROGRAM = False
        print('\nThank you for your purchases!\nYour purchased seats below:\n')
        print(RESERVATIONS)
        print(f'Total purchases: {TOTAL_PURCHASES}$')
        print(f'Account balance: {MYBUDGET.budget}$')
