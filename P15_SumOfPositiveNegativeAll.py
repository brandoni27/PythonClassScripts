# SumOfPositiveNegativeAll.py
# Brandon Washington
# 2/23/2019
# Python 3.6
# Description: Program which determines the sum of all of the positive numbers, negative numbers, and all numbers.


#Holds the input for the numbers.
n1 = int(input("First number?"))
n2 = int(input("Second number?"))
n3 = int(input("Third number?"))
n4 = int(input("Fourth number?"))

#Creating lists to separate the positive and negative numbers
positiveList = list()
negativeList =  list()

#Control flow for adding the positive and negative numbers to there respective lists.
if(n1 < 0):
    negativeList.append(n1)
if(n2 < 0):
    negativeList.append(n2)
if(n3 < 0):
    negativeList.append(n3)
if(n4 < 0):
    negativeList.append(n4)

if(n1 > 0):
    positiveList.append(n1)
if(n2 > 0):
    positiveList.append(n2)
if(n3 > 0):
    positiveList.append(n3)
if(n4 > 0):
    positiveList.append(n4)

#Sum positive list
positiveAnswer = sum(positiveList)

#Sum negative list
negativeAnswer = sum(negativeList)


#Sum of all of the numbers
totalSum = n1+n2+n3+n4

#Printing the totals
print(totalSum)
print(positiveAnswer)
print(negativeAnswer)




'''
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P15_SumOfPositiveNegativeAll.py"
First number?9
Second number?-5
Third number?6
Fourth number?-3
7
15
-8

Process finished with exit code 0

'''