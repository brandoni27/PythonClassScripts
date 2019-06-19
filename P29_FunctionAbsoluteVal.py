# FunctionAbsoluteVal.py
# Brandon Washington
# 3/8/2019
# Python 3.6
# Description: A program to tell you the absolute value of a number.


number = float(input("Input a number to see the absolute value. "))

if(number < 0):
    number = number*-1
    print("The absolute value is: ",number)
else:
    print("The absolute value is: ",number)


'''
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P29_FunctionAbsoluteVal.py"
Input a number to see the absolute value. 0
The absolute value is:  0.0

Process finished with exit code 0


/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P29_FunctionAbsoluteVal.py"
Input a number to see the absolute value. -9
The absolute value is:  9.0

Process finished with exit code 0


/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P29_FunctionAbsoluteVal.py"
Input a number to see the absolute value. 8
The absolute value is:  8.0

Process finished with exit code 0

'''