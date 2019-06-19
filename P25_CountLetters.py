# P25_CountLetters.py
# Brandon Washington
# 5/24/2019
# Python 3.6
# Description: Program that counts letters in a sentence.



sentence = input("Input a sentence.")
count1 = 0
letter1 = input("What letter?")
for i in range(0,len(sentence), 1):
    if sentence[i] == letter1:
        count1 += 1
print("The sentence was,",sentence)
print(letter1, "was found", count1, "times")


'''
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P25_CountLetters.py"
Input a sentence.This is the sentence I am using for this assignment.
What letter?s
The sentence was, This is the sentence I am using for this assignment.
s was found 7 times

Process finished with exit code 0

'''