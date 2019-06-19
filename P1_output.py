# output.py
# Brandon Washington
# 2/1/2019
# Python 3.6
# Description: Program to show output in Python

print('hello world') # single quote
print("hello world") # double quote
print("he\nllo") # \n insert a new line (same as pressing Enter)

# VARIABLES are named storage locations for numbers, strings, lists
# STRING is anything enclosed in quotes "Hello World", that's a string
# NUMBER can be either a FLOAT (Ex: 9.3) or an INTEGER (Ex: 9.0)
# LISTS are things like [1,2,3] or ["Alex", "Stoykov"]
myName = "Brandon" # declare/initialize string variable myNaame
Weight = 270.27
Age= 26
Grades =[90,77,88]
nameZ = ["Brandon", "Washington"]

print ("Hello ", myName)
print ("Your weight is ", Weight, "and your age is ", Age)
print("Your weight is %.2f and your age is %i" %(Weight,Age))
print("Lists: grades =", Grades, "nameZ=",nameZ)
print("This is how you print",end=' ')
print("on the same line")


'''
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P1_output.py"
hello world
hello world
he
llo
Hello  Brandon
Your weight is  270.27 and your age is  26
Your weight is 270.27 and your age is 26
Lists: grades = [90, 77, 88] nameZ= ['Brandon', 'Washington']
This is how you print on the same line

Process finished with exit code 0
'''