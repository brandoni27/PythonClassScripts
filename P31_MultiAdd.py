# MultiAdd.py
# Brandon Washington
# 5/11/2019
# Python 3.6
# Description: Call a function that calls two other functions to perform the logic a*b+c in the proper order.



def add(x,y):
    return x+y
def multi(x,y):
    return x*y
def multiadd(a,b,c):
    p1 = multi(a,b)
    p2 = add(p1,c)
    print(p2)

multiadd(1.1,2.2,3.3)
multiadd(4,4,2)
multiadd(1,1,2)
multiadd(4,2,2)
multiadd(4,3,2)
multiadd(4,6,5)
multiadd(5,4,8)
multiadd(6,4,12)

'''
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P31_MultiAdd.py"
5.720000000000001
18
3
10
14
29
28
36

Process finished with exit code 0
'''