# Dice.py
# Brandon Washington
# 4/27/2019
# Python 3.6
# Description: A dice game that generates two values for you and the computer. Declares winner at the end.

from random import randint

while True:
    d1=randint(1,6)
    d2=randint(1,6)

    keep = input("You rolled %i and %i for a total of %i, keep? y/n" %(d1,d2,d1+d2))
    if keep == 'y':
        break

pc1 = randint(1,6)
pc2 = randint(1,6)
pcTotal = pc1 + pc2
print("The computer rolled a %i" %(pcTotal))
if pc1 + pc2 > d1 + d2:
    print("The computer wins.")
elif pc1 + pc2 < d1 + d2:
    print("You win!")
else:
    print("It's a tie!")

"""
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P22_Dice.py"
You rolled 2 and 6 for a total of 8, keep playing? y/ny
The computer rolled a 7
You win!

Process finished with exit code 0

/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P22_Dice.py"
You rolled 5 and 2 for a total of 7, keep? y/nn
You rolled 6 and 1 for a total of 7, keep? y/nn
You rolled 5 and 5 for a total of 10, keep? y/nn
You rolled 6 and 4 for a total of 10, keep? y/nn
You rolled 1 and 4 for a total of 5, keep? y/nn
You rolled 5 and 2 for a total of 7, keep? y/nn
You rolled 4 and 3 for a total of 7, keep? y/nn
You rolled 3 and 5 for a total of 8, keep? y/nn
You rolled 4 and 1 for a total of 5, keep? y/nn
You rolled 5 and 5 for a total of 10, keep? y/nn
You rolled 5 and 5 for a total of 10, keep? y/nn
You rolled 5 and 5 for a total of 10, keep? y/nn
You rolled 3 and 1 for a total of 4, keep? y/ny
The computer rolled a 10
The computer wins.

Process finished with exit code 0

/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P22_Dice.py"
You rolled 5 and 1 for a total of 6, keep? y/ny
The computer rolled a 6
It's a tie!

Process finished with exit code 0
"""