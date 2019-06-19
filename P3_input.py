# input.py
# Brandon Washington
# 2/1/2019
# Python 3.6
# Description: Program to take input in Python

name = input("Please enter Your Name: ") # this is a string
weightLbs = float(input ("Please enter Your weight in lbs: ")) # a float
age = int (input ("Please enter your age (whole number): " )) # an integer
weightKg = weightLbs*0.453592
title = "Human"

print ("Hello", title, name, "your weight is")
print ( weightLbs, "lbs")
print ("which equals = %.2f" %weightKg, end=' ') # end='' prevents new line
print ("kilograms ")

'''
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P3_input.py"
Please enter Your Name: Brandon
Please enter Your weight in lbs: 270
Please enter your age (whole number): 26
Hello Human Brandon your weight is
270.0 lbs
which equals = 122.47 kilograms 

Process finished with exit code 0
'''