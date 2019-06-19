# P40_SmallestLargestSumAveragewithLists.py
# Brandon Washington
# 5/22/2019
# Python 3.6
# Description: Finds the longest word in a list and counts the number[i] of characters.

from random import randint

x = int(input("How many numbers in the list? "))

print('x=', x)
sum = 0
number = list()
print("First list.")
for i in range(0,x,1):

    number.append(randint(20,50))
    sum += number[i]
    print(number[i], end=',')

    if i == 0:
        smallest = number[i]
        largest = number[i]
    else:
        if number[i] < smallest:
            smallest = number[i]
        elif largest < number[i]:
            largest = number[i]


print('\nsmallest=',smallest)
print('\nlargest=',largest)
print('sum =', sum)
print('avg =',sum/x)
print("\r")
print("Second list.")
for y in range(0,x,1):
    number[y]*=2
    print(number[y], end=',')



'''
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P40_SmallestLargestSumAveragewithLists.py"
How many numbers in the list? 11
x= 11
First list.
23,26,25,21,42,35,50,40,44,21,48,
smallest= 21

largest= 50
sum = 375
avg = 34.09090909090909

Second list.
46,52,50,42,84,70,100,80,88,42,96,
Process finished with exit code 0

'''