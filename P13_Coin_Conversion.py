# Coin_Conversion.py
# Brandon Washington
# 2/20/2019
# Python 3.6
# Description: Program which determines which coins a person has, based on the number of cents they have.


cents = int(input("How many cents do you have?"))

quarters = int(cents/25)

if quarters > 0:
    cents = cents - (quarters * 25)

    print("You have ",quarters, " quarters.")
dimes = int(cents/10)

if dimes > 0:
    cents = cents - (dimes * 10)

    print("You have ",dimes, " dimes.")

nickels = int(cents/5)
if nickels > 0:
    cents = cents - (nickels * 5)

    print("You have ",nickels, " nickels.")

pennies = cents
if pennies > 0:
    print("You have ", pennies, " pennies.")

'''

/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P13_Coin_Conversion.py"
How many cents do you have?66
You have  2  quarters.
You have  1  dimes.
You have  1  nickels.
You have  1  pennies.

Process finished with exit code 0

/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P13_Coin_Conversion.py"
How many cents do you have?16
You have  1  dimes.
You have  1  nickels.
You have  1  pennies.

Process finished with exit code 0


/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P13_Coin_Conversion.py"
How many cents do you have?6
You have  1  nickels.
You have  1  pennies.

Process finished with exit code 0


/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P13_Coin_Conversion.py"
How many cents do you have?4
You have  4  pennies.

Process finished with exit code 0

'''