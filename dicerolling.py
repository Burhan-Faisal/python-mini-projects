import random
print("WELCOME TO THE DICE ROLLING GAME")
choice=input("Roll the dice?(y/n)")
while choice:
    if choice=='y'or choice=='Y':
        die1=random.randint(1,6)
        die2=random.randint(1,6)
        print((die1,die2))
        choice=input("Roll the dice?(y/n)")
    elif choice=='n' or choice=='N':
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice!")
        choice=input("Roll the dice?(y/n)")