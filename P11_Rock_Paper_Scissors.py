# Rock_Paper_Scissors.py
# Brandon Washington
# 2/18/2019
# Python 3.6
# Description: Program which simulates the game Rock, Paper, Scissors

#Import the random library for the Player 2 choice
import random

#Generate the Player 2 choice
randomNum = int(random.randint(1,3))

#Take in the Player 1 input
choice = (str(input("Enter your Rock(R), Paper(P), or Scissors(S): ")))


#Printing the Player 1 choice
print("Player 1: " + choice)

#This prints R,P, or S in response to the generated numbers 1, 2, or 3
if randomNum == 1:
    print("Player 2: R")
elif randomNum == 2:
    print("Player 2: P")
elif randomNum == 3:
    print("Player 2: S")
else:
    print("ERROR")

#The rest of the code is for the deciding logic of the outcome after Player 1 and Player 2 have chosen.

if choice == "R" and randomNum == 1:
    print("It's a tie!")
elif choice == "R" and randomNum == 2:
    print("Paper covers Rock. Player 2 wins!")
elif choice == "R" and randomNum == 3:
    print("Rock breaks scissors. Player 1 wins!")


if choice == "P" and randomNum == 1:
    print("Paper covers Rock. Player 1 wins!")
elif choice == "P" and randomNum == 2:
    print("It's a tie!")
elif choice == "P" and randomNum == 3:
    print("Scissors cuts paper. Player 2 wins!")


if choice == "S" and randomNum == 1:
    print("Rock breaks scissors. Player 2 wins!")
elif choice == "S" and randomNum == 2:
    print("Scissors cuts paper. Player 1 wins!")
elif choice == "S" and randomNum == 3:
    print("It's a tie!")



'''

Enter your Rock(R), Paper(P), or Scissors(S): R
Player 1: R
Player 2: P
Paper covers Rock. Player 2 wins!

Enter your Rock(R), Paper(P), or Scissors(S): R
Player 1: R
Player 2: R
It's a tie!

Enter your Rock(R), Paper(P), or Scissors(S): R
Player 1: R
Player 2: S
Rock breaks scissors. Player 1 wins!



Enter your Rock(R), Paper(P), or Scissors(S): P
Player 1: P
Player 2: P
It's a tie!

Enter your Rock(R), Paper(P), or Scissors(S): P
Player 1: P
Player 2: S
Scissors cuts paper. Player 2 wins!

Enter your Rock(R), Paper(P), or Scissors(S): P
Player 1: P
Player 2: R
Paper covers Rock. Player 1 wins!



Enter your Rock(R), Paper(P), or Scissors(S): S
Player 1: S
Player 2: S
It's a tie!

Enter your Rock(R), Paper(P), or Scissors(S): S
Player 1: S
Player 2: R
Rock breaks scissors. Player 2 wins!

Enter your Rock(R), Paper(P), or Scissors(S): S
Player 1: S
Player 2: P
Scissors cuts paper. Player 1 wins!



'''