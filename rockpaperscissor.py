import random


choose=("Rock","Paper","Scissor")


running=True

while running:
    player=None
    computer=random.choice(choose)

    while player not in choose:
    #entering player choice
     player=input("Enter a choice:")

    #display what player and computer choose
    print(f"Player:{player}")
    print(f"Computer:{computer}")

    if player==computer:
     print("Draw!")

    elif player=="Rock" and computer=="Scissor":
     print("You wins!")

    elif player=="Paper" and computer=="Rock":
     print("You wins!")

    elif player=="Scissor" and computer=="Rock":
     print("You wins!")

    else:
     print("You lose!")


    again=input("Do you want to play again?(y/n):").lower()
    if not again=="y":
     running=False

     print("Thanks for playing")


