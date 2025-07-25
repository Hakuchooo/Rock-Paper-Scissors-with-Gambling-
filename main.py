#Rock, Paper, Scissors
#User Can Deposit Money
#User Can Check Balance
#User Can Use Balance to Gamble
#User Can Lose money
#User Can Make Money
#Cash out Function
from functions import *

def main():

    is_running = True
    balance = 0
    bet_balance = 0
    while is_running:
        print('Welcome to the RPS gambling page')
        print('1 - Check Balance')
        print('2 - Bet Balance')
        print('3 - Deposit Money')
        print('4 - Place Bet')
        print('5 - GAMBLE TIME!!!')
        print('6 - Cash Out')
        print('7 - Exit')
        choice = (input(': '))

        if choice == '1':
            print('BALANCE PAGE')
            check_balance(balance)
        elif choice == '2':
            print('BET BALANCE PAGE')
            betting_balance(bet_balance)
        elif choice == '3':
            print('DEPOSIT PAGE')
            balance = balance + deposit()
        elif choice == '4':
            print('BETTING PAGE')
            placed_bet = place_bet(balance)
            if placed_bet > 0:
                bet_balance = placed_bet
                balance = balance - placed_bet
        elif choice == '5':
            print('GAMBLING PAGE')
            bet_balance = gamble(bet_balance)
        elif choice == '6':
            print('CASH OUT')
            cashed_out = cash_out(bet_balance)
            if cashed_out > 0:
                bet_balance -= cashed_out
                balance += cashed_out
        elif choice == '7':
            is_running = False
        else:
            print('Enter a valid choice')

    else:
        print('Thank You for using the RPS gambling page')
            

if __name__ == "__main__":
    main()
        