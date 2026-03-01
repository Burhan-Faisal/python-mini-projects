import random
print("Lets play rock,paper and scissors🤩")

emojis={
    'r':'🪨',
    'p':'📜',
    's':'✂️'
}
next_game='y'
while True:
    if next_game=='y':
        Computer_choice=random.choice(['r','p','s'])
        choice=input("Rock,Paper or Scissors? (r/p/s) :").lower()

        if (choice=='r')and (Computer_choice=='p'):
            print("You choose ",emojis['r'])
            print("Computer choose ",emojis['p'])
            print("Computer win")

        elif \
        (choice=='p'and Computer_choice=='s'):
            print("You choose ",emojis['p'])
            print("Computer choose ",emojis['s'])
            print("Computer win")

        elif(choice=='s' and Computer_choice=='r'):
            print("You choose ",emojis['s'])
            print("Computer choose ",emojis['r'])
            print("Computer win")

        elif(choice=='r' and Computer_choice=='s'):
            print("You choose ",emojis['r'])
            print("Computer choose ",emojis['s'])
            print("You win")

        elif(choice=='p' and Computer_choice=='r'):
            print("You choose ",emojis['p'])
            print("Computer choose ",emojis['r'])
            print("You win")

        elif(choice=='s'and Computer_choice=='p'):
            print("You choose ",emojis['s'])
            print("Computer choose ",emojis['p'])
            print("You win")

        elif(choice==Computer_choice):
            print("Its a tie")
            
        else:
            print("Please enter a valid option")
            continue

        next_game = input("Continue (y/n) :").lower()

    elif next_game=='n':
        print("Thanks for playing")
        break
    else:
        print("Invalid choice")
        next_game = input("Continue (y/n) :")
