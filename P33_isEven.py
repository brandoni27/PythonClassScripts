# isEven.py
# Brandon Washington
# 3/8/2019
# Python 3.6
# Description: A function that takes a number and returns True or False based on if the number is even or odd.

def isEven(x):
    if(x%2 == 0):
        return True
    elif(x%2 == 1):
        return False


print("The number 3 is even:",isEven(3))
print("The number 4 is even:",isEven(4))

'''
The number 3 is even: False
The number 4 is even: True
'''