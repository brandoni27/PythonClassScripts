# TuitionTable.py
# Brandon Washington
# 2/25/2019
# Python 3.6
# Description: Program which computes tuition after X amount of years.

# Required variables for calculation in the while loop.
tuition = 100000
years = int(input("How many years of tuition do you want to calculate? "))
x = 0
total = 0

# A while loop that calculates the tuition based on how many years of increases they want to calculate.
while(x <= years):
    total = tuition + (tuition  * 0.05)
    tuition = total
    print("$"'{0:.0f}'.format(total))
    x += 1