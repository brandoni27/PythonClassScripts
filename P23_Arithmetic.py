# Arithmetic.py
# Brandon Washington
# 4/27/2019
# Python 3.6
# Description: Helps a person practice addition, subtraction, or multiplication.


from random import randint
while True:
    num1 = randint(0,9)
    num2 = randint(0,9)
    operation = input("Would you like to add(+), sub(-), or mul(*):")

    if operation =="+":
        answer = int (input("What is %i + %i =" %(num1,num2)))
        while answer != num1 + num2:
            answer = int (input("Incorrect, what is %i + %i =" %(num1,num2)))
    if operation =="-":
        answer = int (input("What is %i - %i =" %(num1,num2)))
        while answer != num1 - num2:
            answer = int (input("Incorrect, what is %i - %i =" %(num1,num2)))
    if operation =="*":
        answer = int (input("What is %i * %i =" %(num1,num2)))
        while answer != num1 * num2:
            answer = int (input("Incorrect, what is %i * %i =" %(num1,num2)))
    repeat = input("Would you like to try again? (y/n)")
    if repeat != "y":
        break

'''
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P23_Arithmetic.py"
Would you like to add(+), sub(-), or mul(*):+
What is 4 + 8 =12
Would you like to try again? (y/n)y
Would you like to add(+), sub(-), or mul(*):-
What is 7 - 8 =-1
Would you like to try again? (y/n)y
Would you like to add(+), sub(-), or mul(*):*
What is 1 * 3 =3
Would you like to try again? (y/n)y
Would you like to add(+), sub(-), or mul(*):+
What is 5 + 3 =4
Incorrect, what is 5 + 3 =8
Would you like to try again? (y/n)y
Would you like to add(+), sub(-), or mul(*):-
What is 6 - 3 =4
Incorrect, what is 6 - 3 =3
Would you like to try again? (y/n)y
Would you like to add(+), sub(-), or mul(*):*
What is 3 * 6 =5
Incorrect, what is 3 * 6 =18
Would you like to try again? (y/n)n

Process finished with exit code 0
'''