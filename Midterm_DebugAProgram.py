# Midterm_DebugAProgram.py
# Brandon Washington
# 3/8/2019
# Python 3.6
# Debug the program so that it works as shown in the test run.

num = float(input("Please enter a number: "))

def isEven(num): # should have a parameter
  if(num%2 == 0):
     return True
  elif(num%2 != 0):
     return False

def main( ): # needs to be called first
   print ("The number %d is even: %s" % (num, str(isEven(num))))

main()

'''

Please enter a number: 5
The number 5 is even: False


Please enter a number: 8
The number 8 is even: True

'''