from termcolor import colored,cprint
board = [
  [' ', ' ', ' '],
  [' ', ' ', ' '],
  [' ', ' ', ' ']
]

X='X'
O='O'

score_x,score_y=0,0

def print_board():
    line ="---+---+---"
    print(line)
    for row in board:
        print(f'{cell(row[0])}  | {cell(row[1])} | {cell(row[2])}')
        print(line)


def cell(move):
    if move==X:
        return colored(move,'red')
    else:
        return colored(move,'white')

def get_positon(label):
     while True:
        try:
            position=int(input(f"Enter the {label}(0-2)"))
            if position<0 or position>2:
                raise ValueError
            return position
        except ValueError:
            cprint("Invalid Choice !",'red')
        except KeyboardInterrupt:
            cprint("Game Restart")


def get_move(current):
    while True:
        row=get_positon("row")
        column=get_positon("column")
        if board[row][column] == ' ':
            board[row][column]=current
            break
        else:
            print("This spot is already occupied 😓!")

def is_fullboard():
    for row in board:
        if ' ' in row:
            return False
    return True


def is_winner():
    for row in board:
        if row[0]==row[1]==row[2] !=' ':
            return True
    for column in range(3):
        if board[0][column]==board[1][column]==board[2][column] !=' ':
            return True
    if (board[0][0]==board[1][1]==board[2][2] !=' ' or
        board[0][2]==board[1][1]==board[2][0] !=' '):
        return True

def next_game():
    another_game=input("Want to play another game? yes /no").strip().lower()
    if another_game=='yes':
        return True
    else:
        return False
def update_score(current):
    if current==X:
        global score_x
        global score_y
        score_x+=1
    else:
        score_y+=1

def reset_board():
    return [[' ']*3 for _ in range(3)]

def main():
    print("Let's play the Tic_Tac_Toe🤩")
    print_board()
    current_player=X
    while True:
        print(f"Player {current_player}'s turn ")
        get_move(current_player)
        print_board()

        if(is_winner()):
            print(f'Player{current_player} is the WINNNER🥳')
            update_score(current_player)
            if(next_game()):
                global board
                board=reset_board()
                continue
            else:
                print(f"No of games won by X are {score_x}")
                print(f"No of games won by O are {score_y}")
                break   
        if (is_fullboard()):
            print(f'Match Tied')
            if(next_game()):
                global board
                board=reset_board()
                continue
            else:
                break   
        current_player=O if current_player==X else X



main()




    
