# P40_SmallestLargestSumAveragewithLists.py
# Brandon Washington
# 5/22/2019
# Python 3.6
# Description: Wrote classes to find the smalles, largest, sum, and average of the list.


def sum(myList):
    total = 0
    for i in range(0,len(myList),1):
        total += myList[i]
    return total

def average(myList):
    total = 0
    for i in range(0,len(myList),1):
        total += myList[i]
        ave = total/len(myList)
    return ave

def min(myList):

    for i in range(0,len(myList),1):
        if 0 == i:
            smallest = myList[i]
        else:
            if myList[i] < smallest:
                smallest = myList[i]
    return smallest

def max(myList):
    for i in range(0,len(myList),1):
        if 0 == i:
            largest = myList[i]
        else:
            if myList[i] > largest:
                largest = myList[i]
    return largest

def main():
    aList = [2,4,6,7,10,13,16,19,20,23,24,26,30]
    s = sum(aList)
    print("The sum of numbers inside the list", aList, "is:",s)
    print('The average is',average(aList))
    print('The minimum is',min(aList))
    print('The maximum is',max(aList))

main()

'''
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P42_sumAverageMinMax.py"
The sum of number inside the list [2, 4, 6, 7, 10, 13, 16, 19, 20, 23, 24, 26, 30] is: 200
The average is 15.384615384615385
The minimum is 2
The maximum is 30

Process finished with exit code 0
'''