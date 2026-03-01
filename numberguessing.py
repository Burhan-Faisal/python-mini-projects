import random
number=random.randint(1,100)
print("Welcome to the number guesssing game")
while True:
    try:
        guess_number=int(input("Enter a number b/w 1 and 100 "))
        if (guess_number==number):
            print("Congratulations! you have guessed the number")
            break
        elif(guess_number>number):
            print("Too high !")
        elif(guess_number<number):
            print("Too low !")
    except ValueError:
        print("Please enter a valid number")