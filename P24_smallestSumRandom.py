# smallestSumRandom.py
# Brandon Washington
# 4/27/2019
# Python 3.6
# Description: Finds the smallest, largest, sum and average of the set.

from random import randint

X = randint(10,15)

print('x=',X)
summ = 0
for i in range(0,X,1):
    number =randint(20,50)
    summ += number
    print(number, end =',')

    if i == 0:
        smallest = number
        largest = number
    else:
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number



print ('\nsmallest =',smallest)
print ('\nlargest =', largest)
print ('sum =', summ)
print ('avg =', summ/X)
