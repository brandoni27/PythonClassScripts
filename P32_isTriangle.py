# isTriangle.py
# Brandon Washington
# 5/11/2019
# Python 3.6
# Description: Tells you whether a set of lengths could form a triangle.

def is_triangle(a,b,c):
    if (a > b + c) or (b > a + c) or (c > a + b):
        print("No")
    else:
        print("Yes")

is_triangle(3,4,5)
is_triangle(9,1,1)
is_triangle(5,5,5)

'''
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P32_isTriangle.py"
Yes
No
Yes

Process finished with exit code 0
'''