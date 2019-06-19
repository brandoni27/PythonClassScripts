# sumDouble.py
# Brandon Washington
# 3/8/2019
# Python 3.6
# Description: A function that takes two numbers and returns the sum. If the numbers are equal, then the sum is doubled and printed.

def sumDouble(a,b):
    answer = a + b
    if(a == b):
        answer = answer*2
        print(answer)
    else:
        return answer


print(sumDouble(8,4))
sumDouble(7,7)

'''

12
28

'''