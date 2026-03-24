import random,termcolor
from wordguess import next_game

symbols=('🍒','⭐','🎩')

def get_starting_balance():
    while True:
        try:
            balance=int (input("Enter your starting balance : $"))
            if balance<=0:
                print("Balance must be a positive Number !")
            else:
                return balance
        except ValueError:
            termcolor.cprint("Enter a valid balance !",'red')

def place_bet(balance):
    while True:
        try:
            bet=int(input("Enter Your bet Amount : $"))
            if 0<=bet<=balance:
                return bet
            termcolor.cprint(f"Bet Amount must be b/w $1 and ${balance}")
        except ValueError:
            termcolor.cprint("Invalid Amount")


def is_winner(spin,bet):
    if spin[0]==spin[1]==spin[2]:
        return 10*bet
    elif spin[0]==spin[1] or spin[1]==spin[2] or spin[0]==spin[2]:
        return 2*bet
    else:
        return None
    
def main():
    start_balance=get_starting_balance()
    current_balance=start_balance
    termcolor.cprint("Welcome to the Slot machine Game",'green',attrs=['bold'])
    print(f"You start with the balance of ${start_balance}.\n\n")

    while True:
        print(f"Current Balance: ${current_balance}")
        bet=place_bet(current_balance)
        spin=[random.choice(symbols) for _ in range(3)]
        payout=is_winner(spin,bet)
        print(' | '.join(spin))

        if(payout):
            print(f"You Won ${payout}")
            current_balance+=payout
        else:
            termcolor.cprint(f'You have lost your bet ${bet}😓','red')
            current_balance-=bet
        
        if current_balance<=0:
            termcolor.cprint("You're out of money! Game over.", 'red', attrs=['bold'])
            break

        game=next_game() # Importing the function from our previous project file(wordguess.py)

        if game:
            continue
        else:
            print(f"You walk away with ${current_balance} .")
            return
            
    
if __name__=='__main__':       
    main()
