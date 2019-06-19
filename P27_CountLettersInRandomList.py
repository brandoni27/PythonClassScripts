# CountLettersInRandomList.py
# Brandon Washington
# 4/27/2019
# Python 3.6
# Description: Counts letters in a Random List of Letters.


from random import randint

x = randint(50,75)
empty_list=[]
countB = 0
for i in range(0,x,1):
    ascii = randint(65,70)
    empty_list.append(chr(ascii))
    if ascii ==66:
        countB+=1
print('Made a list of',x,'letters')
print(empty_list)
print('the letter "B" appears',countB,'times')

'''
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P27_CountLettersInRandomList.py"
Made a list of 59 letters
['D', 'A', 'C', 'E', 'A', 'F', 'C', 'E', 'E', 'F', 'D', 'F', 'D', 'E', 'E', 'C', 'D', 'E', 'F', 'B', 'A', 'A', 'B', 'E', 'E', 'D', 'B', 'B', 'C', 'C', 'C', 'F', 'A', 'C', 'E', 'E', 'E', 'D', 'B', 'A', 'F', 'D', 'E', 'D', 'A', 'C', 'F', 'A', 'A', 'E', 'B', 'E', 'A', 'B', 'C', 'C', 'B', 'A', 'C']
the letter "B" appears 8 times

Process finished with exit code 0

/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P27_CountLettersInRandomList.py"
Made a list of 50 letters
['F', 'A', 'C', 'C', 'E', 'A', 'F', 'B', 'A', 'C', 'B', 'F', 'E', 'B', 'A', 'D', 'E', 'B', 'B', 'A', 'B', 'A', 'B', 'D', 'F', 'A', 'A', 'A', 'C', 'B', 'B', 'A', 'A', 'A', 'F', 'A', 'C', 'A', 'C', 'D', 'D', 'C', 'A', 'D', 'E', 'F', 'F', 'A', 'B', 'E']
the letter "B" appears 10 times

Process finished with exit code 0

/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P27_CountLettersInRandomList.py"
Made a list of 75 letters
['D', 'C', 'D', 'A', 'B', 'C', 'B', 'E', 'C', 'B', 'E', 'F', 'E', 'E', 'C', 'C', 'C', 'F', 'F', 'C', 'C', 'A', 'C', 'D', 'D', 'E', 'D', 'A', 'F', 'F', 'F', 'F', 'D', 'A', 'B', 'D', 'C', 'D', 'B', 'D', 'D', 'D', 'A', 'F', 'E', 'E', 'D', 'D', 'F', 'F', 'F', 'D', 'E', 'E', 'A', 'A', 'A', 'A', 'F', 'F', 'A', 'E', 'A', 'A', 'F', 'B', 'C', 'C', 'D', 'C', 'F', 'F', 'C', 'F', 'F']
the letter "B" appears 6 times

Process finished with exit code 0
'''