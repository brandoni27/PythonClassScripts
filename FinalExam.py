# FinalExam.py
# Brandon Washington
# 5/24/2019
# Python 3.6
# Description: Final Exam

#Making the unsorted list.
from random import randint
numList = []
for i in range(0,10,1):
    numList.append(randint(20,30))

print("Unsorted List :",numList)

#Sorting the list using bubblesort method.

for j in range (0, len(numList), 1):
  for i in range (0, len(numList)-1, 1):
    if numList[i] > numList[i+1]:
      temp = numList[i]
      numList[i] = numList[i+1]
      numList[i+1] = temp

print("Sorted List :",numList)

#Finding the Sum, Max, and Min.

sum=0
for i in range(0,len(numList),1):
    sum += numList[i]
    if i == 0:
        smallest = numList[i]
        largest = numList[i]
    else:
        if numList[i] < smallest:
            smallest = numList[i]
        elif largest < numList[i]:
            largest = numList[i]

# Show Median
median = (numList[4]+numList[5])/2

# How many divisible by 2
divisibleBy2 = 0
for i in range(0,len(numList),1):
    if numList[i] % 2 == 0:
        divisibleBy2 += 1


print("The Sum is :",sum)
print("The Minimum is :",smallest)
print("The Maximum is :",largest)
print('The Average is :', sum/len(numList))
print("The Median is :", median)
print(divisibleBy2,"numbers are evenly divisible by 2.")


'''
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/FinalExam.py"
Unsorted List : [27, 22, 27, 28, 28, 27, 21, 30, 20, 28]
Sorted List : [20, 21, 22, 27, 27, 27, 28, 28, 28, 30]
The Sum is : 258
The Minimum is : 20
The Maximum is : 30
The Average is : 25.8
The Median is : 27.0
6 numbers are evenly divisible by 2.

Process finished with exit code 0
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/FinalExam.py"
Unsorted List : [29, 20, 23, 21, 26, 25, 27, 27, 22, 25]
Sorted List : [20, 21, 22, 23, 25, 25, 26, 27, 27, 29]
The Sum is : 245
The Minimum is : 20
The Maximum is : 29
The Average is : 24.5
The Median is : 25.0
3 numbers are evenly divisible by 2.

Process finished with exit code 0
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/FinalExam.py"
Unsorted List : [27, 25, 26, 26, 29, 23, 23, 24, 26, 29]
Sorted List : [23, 23, 24, 25, 26, 26, 26, 27, 29, 29]
The Sum is : 258
The Minimum is : 23
The Maximum is : 29
The Average is : 25.8
The Median is : 26.0
4 numbers are evenly divisible by 2.

Process finished with exit code 0
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/FinalExam.py"
Unsorted List : [21, 22, 30, 29, 27, 22, 23, 21, 28, 26]
Sorted List : [21, 21, 22, 22, 23, 26, 27, 28, 29, 30]
The Sum is : 249
The Minimum is : 21
The Maximum is : 30
The Average is : 24.9
The Median is : 24.5
5 numbers are evenly divisible by 2.

Process finished with exit code 0

'''