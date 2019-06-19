# User_Height_Message.py
# Brandon Washington
# 2/2/2019
# Python 3.6
# Description: Program which height in total inches and displays a message based off of the amount.

#Asking for user input
print("Please enter your height ")
feet = int(input("feet: "))
inches = int(input("inches: "))

#Calculate total_inches
total_inches = feet * 12 + inches

#Give user the message
if total_inches > 72:
    print("You are tall")

if total_inches < 72 and total_inches > 60:
    print("You are average")

if total_inches < 60:
    print("You are vertically challenged")



'''
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P9_User_Height_Message.py"
Please enter your height 
feet: 6
inches: 3
You are tall

Process finished with exit code 0






/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P9_User_Height_Message.py"
Please enter your height 
feet: 5
inches: 3
You are average

Process finished with exit code 0





/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P9_User_Height_Message.py"
Please enter your height 
feet: 4
inches: 3
You are vertically challenged

Process finished with exit code 0
'''