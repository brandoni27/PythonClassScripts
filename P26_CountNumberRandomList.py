# P25_CountLetters.py
# Brandon Washington
# 5/24/2019
# Python 3.6
# Description: Program that creates a list of random numbers and counts how many times the number 3 appears in the list.


import random
x = random.randint(15,20)
aList = [] # make an empty list
for i in range(0,x,1):
    randomNum = random.randint(2,5)
    aList.append(randomNum) # add random numbers to the list
print(aList)

count3 = 0
for i in range(0,x,1):
    if aList[i] == 3: # if you find a 3
        count3 += 1 # add 1 to count3

print(3, "was found", count3, "times")


'''
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P26_CountNumberRandomList.py"
[2, 2, 5, 5, 2, 2, 5, 3, 2, 5, 5, 5, 3, 2, 2, 5, 2]
3 was found 2 times

Process finished with exit code 0
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P26_CountNumberRandomList.py"
[4, 3, 2, 5, 2, 5, 3, 3, 3, 2, 2, 2, 4, 4, 3]
3 was found 5 times

Process finished with exit code 0
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P26_CountNumberRandomList.py"
[5, 3, 5, 2, 4, 4, 2, 2, 5, 5, 3, 2, 4, 4, 5, 4]
3 was found 2 times

Process finished with exit code 0
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P26_CountNumberRandomList.py"
[4, 5, 2, 2, 2, 4, 4, 3, 2, 5, 5, 3, 2, 3, 3, 4, 3]
3 was found 5 times

Process finished with exit code 0
'''