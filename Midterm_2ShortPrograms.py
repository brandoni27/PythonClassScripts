# Midterm_2ShortPrograms.py
# Brandon Washington
# 3/8/2019
# Python 3.6
# One function calculates speed, the other function calculates the median.

def speedCalc(d,t):
    speed = d/t
    print("Speed = ","{0:.2f}".format(speed),"mph")

speedCalc(90,3.4)
speedCalc(120,4)
speedCalc(900,3)

def median(a,b,c):
    if(a < b and b < c):
        print(b)
    elif (c < b and b < a):
        print(b)
    elif(b < a and a < c):
        print(a)
    elif (c < a and a < b):
        print(a)
    elif(b < c and c < a):
        print(c)
    elif (a < c and c < b):
        print(c)
    else:
        print("There is no median. ")

median(1,2,3)
median(2,1,3)
median(3,2,1)
median(1,3,2)
median(2,3,1)
median(3,1,2)

'''

Speed =  26.47 mph
Speed =  30.00 mph
Speed =  300.00 mph
2
2
2
2
2
2

'''
