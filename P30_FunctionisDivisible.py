# FunctionisDivisible.py
# Brandon Washington
# 3/8/2019
# Python 3.6
# Description: A function that takes two numbers and tells you if they are evenly divisible or not.




def isDivisible(a,b):
    if(a%b == 0):
        return True
    elif(a%b != 0):
        return False

print("9 and 3 are evenly divisible:",isDivisible(9,3))
print("8 and 3 are evenly divisible:",isDivisible(8,3))

'''
9 and 3 are evenly divisible: True
8 and 3 are evenly divisible: False

'''