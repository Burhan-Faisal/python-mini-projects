import random,re


def display_word(secret_word,guessed_letters):
    for letter in secret_word:
        if letter in guessed_letters:
            print(letter,end='')
        else:
            print('_',end='')
    print()


def get_hint(word,guessed_letters):
    random_hints=[]
    while True: 
        print("Do You want Hint? (y/n)      *** You can Use This Option Two Times in each game. ***")
        choice=input().strip().lower()

        if choice=='y':
            for index,letter in enumerate(word,start=1):
                if letter not in guessed_letters:
                    random_hints.append((index,letter))
                    
            index,hint=random.choice(random_hints)
            print(f"Letter at position {index} is {hint}")  
            return True
        
        elif choice=='n':
            return False
        
        else:
            print("Please enter a valid Choice")


def is_guessed(word,guess_list):
    for letter in word:
        if letter not in guess_list:
            return False
    return True


def get_guess(guessed_letters):
  while True:
    guess = input('Enter a letter: ').lower()
    if len(guess) != 1:
      print('Enter only one letter.')
    elif not re.search('[a-z]', guess):
      print('Enter only letters from a to z.')
    elif guess in guessed_letters:
      print('You already guessed that letter.')
    else:
      return guess
    
def next_game():
    while True:
        choice=input("Do You Want to Play Next game? (y/n)").strip().lower()
        if choice=='y':
            return True
        elif choice=='n':
            return False
        else:
            print(' Invalid Choice !')

def play_game():
    games_won,games_loss=0,0
    max_attempts=7
    print("-------Let's Play a Word Guessing Game-------")

    while True: 
        difficulty_level=input("Please Enter The Difficulty Level : \n (Beginner/Advance)").strip().lower()

        if difficulty_level=='beginner':
            with open('short_words.txt','r') as f:
                data=f.read().split()
                break

        elif difficulty_level=='advance':
            with open('long_words.txt','r') as f:
                data=f.read().split()
                break
        else:
            print("Enter a Valid Option !")
    
    while True:
        guessed_letters=[]
        attempts=0
        hints=0
        word=random.choice(data) 
        display_word(word,guessed_letters)

        while attempts<max_attempts:  
                    
            guess=get_guess(guessed_letters)
            guessed_letters.append(guess)

            if guess in word:
                print("Good Guess!")
                display_word(word,guessed_letters)
                if (is_guessed(word,guessed_letters)):
                    games_won+=1
                    print("Congratulations You have Guessed the word!")
                    break 

            else:
                print("Wrong Guess!")
                attempts+=1
                display_word(word,guessed_letters)
                print(f"Attempts left : {max_attempts-attempts}")

                if hints>2:
                    if(get_hint(word,guessed_letters)):
                        hints+=1

                if attempts==max_attempts:
                    games_loss+=1
                    print("You are out of attempts!")
                    print(f"The correct word is {word} .")
                    break

        if (next_game()):
            continue
        else :
            print(f"TOTAL GAMES WON :{games_won}\n TOTAL GAMES LOSS : {games_loss}")
            return



if __name__=='__main__':
    play_game()