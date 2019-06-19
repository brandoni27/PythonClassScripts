# PennyOrMillion.py
# Brandon Washington
# 3/4/2019
# Python 3.6
# Description: A program to tell you the difference between taking a million dollars, or taking a penny that doubles every day.

million = 1000000
amount = 0.01
days = 1

while (days != 31):
    amount = amount + amount
    if(days == 30):
        print("The amount of doubling a penny after 30 days: ",'{:.{prec}f}'.format(amount, prec=2))
    days+=1
print("The amount of accepting the one million dollars: ", million)
print("You make",amount - million,"more dollars by taking the penny.")

'''
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P21_PennyOrMillion.py"
The amount of doubling a penny after 30 days:  10737418.24
The amount of accepting the one million dollars:  1000000
You make 9737418.24 more dollars by taking the penny.

Process finished with exit code 0
'''