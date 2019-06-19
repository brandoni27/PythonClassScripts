# SumPositiveNegativeNumbers.py
# Brandon Washington
# 3/8/2019
# Python 3.6
# Description: A program to tell you the sum of positive, negative and all numbers.




restart = 'y'
while restart == 'y':
    if restart == 'y':

        x = 0
        choice = int(input("How many numbers would you like to enter? "))
        sumNegative = []
        sumPositive = []
        sumAll = []
        while x < choice:
            x += 1
            answer = float(input("Please enter number %d " %(x)))
            sumAll.append(answer)
            if(answer < 0):
                sumNegative.append(answer)
            if(answer > 0):
                sumPositive.append(answer)

        print("The sum of the negatives is ", sum(sumNegative))
        print("The sum of the positives is ", sum(sumPositive))
        print("The sum of all of the numbers is ", sum(sumAll))


        restart = str(input("Would you like to run this again? (y)/(n)"))
    elif restart == 'n':
        break

'''
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P20_SumPositiveNegativeNumbers.py"
How many numbers would you like to enter? 5
Please enter number 1 8
Please enter number 2 3
Please enter number 3 -6
Please enter number 4 -4
Please enter number 5 10
The sum of the negatives is  -10.0
The sum of the positives is  21.0
The sum of all of the numbers is  11.0
Would you like to run this again? (y)/(n)y
How many numbers would you like to enter? 2
Please enter number 1 -10
Please enter number 2 9
The sum of the negatives is  -10.0
The sum of the positives is  9.0
The sum of all of the numbers is  -1.0
Would you like to run this again? (y)/(n)n

Process finished with exit code 0
'''

'''






'''