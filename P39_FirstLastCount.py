# FirstLastCount.py
# Brandon Washington
# 5/22/2019
# Python 3.6
# Description: Finds the longest word in a list and counts the number of characters.



sentence = input('enter sentence')
words = sentence.split()
print('words= ',words)
first = words[0]
print(len(words))
last = words[len(words)-1]
print('This is the last word',last)
print('This is the first word', first)

word = input('enter word')
count = 0
for i in range(0,len(words),1):
    if words[i] == word:
        count += 1
print('The word',word,'appears',count,'times.')

'''
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P39_FirstLastCount.py"
enter sentence this is the sentence that I am entering into the system
words=  ['this', 'is', 'the', 'sentence', 'that', 'I', 'am', 'entering', 'into', 'the', 'system']
11
This is the last word system
This is the first word this
enter wordthe
The word the appears 2 times.

Process finished with exit code 0
'''