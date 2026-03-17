import random

def get_number():
    numbers=random.sample(range(1,10),4)
    unique_number=''.join(map(str,numbers))
    return unique_number

def cow(guess,number):
    count=0
    for i in guess:
        if i in number:
            count+=1
    return count 


def bull(guess,number):
    count=0
    for i ,j in zip(number,guess):
        if i==j:
            count+=1
    return count

def give_hint(number):
    position=random.randint(0,3)
    print(f"Digit at position {position+1} is {number[position]} ")

def play_game():
    number=get_number()
    attempts=0
    print("I have generated a 4 digit number with unique digits. Try to guess it !")
    while True:
        try:
            guess=(input("Guess : "))
            if guess.isdigit() and len(guess)==4:
                if guess==number:
                    print("Congratulations! you have guessed the number")
                    break
                bulls=bull(guess,number)
                cows=cow(guess,number)-bulls
                print(f"{cows} cows , {bulls} bulls")
                attempts+=1
                if attempts==5:
                    hint=give_hint(number)
            else:
                raise ValueError
        except ValueError:
            print("Invalid Guess !")


if __name__ == '__main__':
    play_game()