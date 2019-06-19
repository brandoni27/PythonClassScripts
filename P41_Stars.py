# Brandon Washington
# 5/22/2019
# Python 3.6
# Description: Prints rows leading up to the number of crosses requested.

def stars(numCrosses):
    for row in range(0,numCrosses,1):
        print('*',end='')
        for x in range(0,row,1):
            print('*',end='')
        print()
stars(10)
stars(20)

'''
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 /Users/Brando/Downloads/P41_Stars.py
*
**
***
****
*****
******
*******
********
*********
**********
*
**
***
****
*****
******
*******
********
*********
**********
***********
************
*************
**************
***************
****************
*****************
******************
*******************
********************
Process finished with exit code 0
'''