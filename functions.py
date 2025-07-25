import random


def check_balance():
    print(f'Balance: {balance}')


def betting_balance():
    print(f'Bet Balance: {bet_balance}')


def deposit():
    print('Deposit Amount')
    deposit_amount = float(input('PHP: '))
    if deposit_amount <= 0:
        print('Enter a valid deposit amount')
        return 0
    else:
        print(f'PHP: {deposit_amount} has been added to your account')
        return deposit_amount
    
def place_bet():
    print('GAMBLING TIME BABY!!!')

    print('How Much Do You want to bet?')
    bet_amount = float(input('PHP: '))
    if bet_amount <= 0:
        print('Invalid amount')
        return 0
    elif bet_amount > balance:
        print('Invalid amount')
        return 0
        
    else:
        print(f'Bet placed PHP: {bet_amount}')
        return bet_amount

def gamble():
        global bet_balance
        global balance
        win_con = {
        'Rock': 'Scissors',
        'Paper': 'Rock',
        'Scissors': 'Paper'
    }
        
        if bet_balance > 0:
            print(f'You are betting {bet_balance}')
            print('Rock')
            print('Paper')
            print('Scissors')
            player_choice = input('Choice: ')

            random_choice = random.choice(list(win_con.keys()))

            if win_con[player_choice] == random_choice:
                print(f'You chose: {player_choice} Apponent chooses: {random_choice}')
                print('OUTCOME: YOU WIN')
                bet_balance *= 2
            elif player_choice == random_choice:
                print(f'You chose: {player_choice} Apponent chooses: {random_choice}')
                print('OUTCOME: DRAW')
                bet_balance = bet_balance
            else:
                print(f'You chose: {player_choice} Apponent chooses: {random_choice}')
                print('OUTCOME: YOU LOSE')
                bet_balance *= 0
        else:
            print('Insufficient betting amount')

def cash_out():
    print(f'Available Balance to cash out: {bet_balance}')
    cashout_Amount = float(input('PHP: '))
    if cashout_Amount > bet_balance:
        print(f'Insufficient Bet Balance: {bet_balance}')
        return 0 
    else:
        print(f'PHP: {cashout_Amount} succesfully cashed out')
        return cashout_Amount