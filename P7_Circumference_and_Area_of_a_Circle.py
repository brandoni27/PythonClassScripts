# Circumference_and_Area_of_a_Circle.py
# Brandon Washington
# 2/4/2019
# Python 3.6
# Description: Program which computes the radius, circumference, and area of a circle.

#Defined pi as a variable
pi = 3.1415

#Asking user to input the radius of a circle
radius = float(input("What is the radius"))

#Calculating the circumference and area
circumference = float(radius * 2 * pi)
area = float(radius * radius * pi)

#Printing the output, formatted to one decimal place
print("A circle with a radius of %.1f inches has" %radius)
print("circumference: %.1f inches" %circumference)
print("area: %.1f sq. inches" %area)


'''
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P7_Circumference_and_Area_of_a_Circle.py"
What is the radius84
A circle with a radius of 84.0 inches has
circumference: 527.8 inches
area: 22166.4 sq. inches

Process finished with exit code 0
'''