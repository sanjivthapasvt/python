from random import randint
play = True
while play:
    user = int(input("Enter number in between 1 and 10: "))
    computer = randint(0,10)
    print(f"You choosed {user}. Computer Choosed {computer}")
    if (computer == user):
        print("You lost")
    else:
        print("You win")

    playagain = input("Would you like to play again? (y/n)").capitalize()
    if playagain != "Y":
        play = False

print("Thank you for playing the game!!")