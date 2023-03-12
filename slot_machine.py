#Slot Machine
import random

max_lines = 3 #maximum number of lines on which user can bet
max_bet = 100 #maximum amount in dollars user can bet
min_bet = 1 #minimum amount in dollars user can bet 
rows = 3 
cols = 3

symbol_count={
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value={
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

#check the winnings
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
   
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]* bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

#generating spin
def spin(rows,cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for i in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

#printing the line
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row] , end="|")
            else:
                print(column[row], end="")
        print()

#Geeting the amount user will have to play
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a valid amount to begin")
    return amount

#getting number of line
def get_lines():
   while True:
        lines = input("Enter the number of lines to bet on (1-"+str(max_lines)+")? ")
        
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= max_lines: #checking in between values
                break
            else:
                print("Enter a valid number of line")
        else:
            print("Please enter a number.")
   return lines 

#get the betting amount from the user
def get_bet():
   while True:
        bet = input("How much would you like to bet on each line? $")
        
        if bet.isdigit():
            bet = int(bet)
            if min_bet <= bet <= max_bet: #checking in between values
                break
            else:
#another way of concatinating put f in beginning of string and place your variable in {}
                print(f"Amount must be between ${min_bet} - ${max_bet}.") 

        else:
            print("Please enter a number.")
   
   return bet 
    
#playing the game
def game(balance):
    lines = get_lines()
    #checking that the total bet must be less than the balance(amount deposited)
    while True:
        bet = get_bet()
        total_bet = bet*lines
        if total_bet > balance:
            print(f"You do not have enough amount to bet\nYour current balance is ${balance}")
        else:
            break
    print("*******************************")    
    print(f"You have deposited ${balance}") 
    print(f"You will be betting ${bet} on {lines} lines.\nTotal bet is ${total_bet}.")

    slot = spin(rows,cols,symbol_count)
    print_slot_machine(slot)

    winnings, winning_lines = check_winnings(slot,lines,bet,symbol_value)
    print(f"You won {winnings}.")
    print(f"You won on line:", *winning_lines)

    return winnings - total_bet

#whenever need to restart we can call this main function
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play or q to quit")
        if answer == "q":
            break
        balance += game(balance)
        print("__________________________________")
    
    print(f"You left with {balance}")

   
    
main()