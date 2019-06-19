# LetterGradesWithInputValidation.py
# Brandon Washington
# 2/18/2019
# Python 3.6
# Description: Program which computes the sum and product of two numbers entered by the user.

print("Please enter your score")
score = int(input("score: "))

if score < 0:
    print("ERROR. Please enter a score between 0 and 100")
elif score > 100:
    print("You have a 'A+' Incredible!!!")
elif score > 90 and score < 100:
    print("You have an 'A'")
elif score > 80 and score < 90:
    print("You have a 'B'")
elif score > 70 and score < 80:
    print("You have a 'C'")
elif score > 60 and score < 70:
    print("You have a 'D'")
elif score < 60:
    print("You have a 'F'")

'''
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P10_LetterGradesWithInputValidation.py"
Please enter your score
score: 110
You have a 'A+' Incredible!!!

Process finished with exit code 0





/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P10_LetterGradesWithInputValidation.py"
Please enter your score
score: 95
You have an 'A'




Process finished with exit code 0

/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P10_LetterGradesWithInputValidation.py"
Please enter your score
score: 85
You have a 'B'





Process finished with exit code 0

/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P10_LetterGradesWithInputValidation.py"
Please enter your score
score: 75
You have a 'C'

Process finished with exit code 0




/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P10_LetterGradesWithInputValidation.py"
Please enter your score
score: 65
You have a 'D'

Process finished with exit code 0



/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P10_LetterGradesWithInputValidation.py"
Please enter your score
score: 57
You have a 'F'

Process finished with exit code 0




/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P10_LetterGradesWithInputValidation.py"
Please enter your score
score: -24
ERROR. Please enter a score between 0 and 100

Process finished with exit code 0




'''