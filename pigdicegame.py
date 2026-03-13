import termcolor,random

score={

}

def is_winner(player):
    if score[player]>=30:
        return True
    else:
        return False

def get_turn():
    return random.randint(1,6)


def add_players(total_players):
    for i in range(1,total_players+1):
        score[f"Player {i}"]=0

def print_scores():
    print("\nCurrent Scores:")
    for player, points in score.items():
        print(f"  {player}: {points}")


def play_game():
    print("----------Let's Play PigDice Game-----------")
    total_players=int(input("How many players do you want to play? "))
    add_players(total_players)

    while True:
        for i in range(1,total_players+1):
            print(f"Player {i}'s turn ")
            turn_score=0                    


            while True:
                roll=get_turn()
                print(f"You rolled a {roll}")

                if roll==1:
                    termcolor.cprint("Rolled a 1. Turn Ended !",'red')
                    turn_score=0
                    print(f"You scored a total {turn_score} this turn.")
                    print_scores()
                    break

                turn_score+=roll
                roll_again=input("Roll Again ? (y/n)").strip().lower()

                if roll_again!='y':
                    score[f"Player {i}"] += turn_score
                    print(f"You scored a total {turn_score} this turn.")
                    print_scores()
                    break
                
            if (is_winner(f'Player {i}')):
                print_scores()
                termcolor.cprint(f"PLayer {i} is the Winner 🥳",'green')
                return
                    
                

play_game()