# Compute_Height.py
# Brandon Washington
# 2/4/2019
# Python 3.6
# Description: Program which computes someone's height in inches after having been given the input of feet and inches.



#This statement ask the user for height in feet
feet = float(input("How tall are you in feet?"))

#This statement ask the user for height in inches
inches = float(input("How tall are you in inches?"))

#This statement calculates the total inches
totalInches = 12 * feet + inches

#This statement prints the results and formats them
print( '%.0f feet %.0f inch(es) = %.0f inches' %(feet, inches, totalInches))

'''
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P6_Compute_Height.py"
How tall are you in feet?10
How tall are you in inches?10
10 feet 10 inch(es) = 130 inches

Process finished with exit code 0
'''