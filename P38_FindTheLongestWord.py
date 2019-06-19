# FindTheLongestWord.py
# Brandon Washington
# 5/22/2019
# Python 3.6
# Description: Finds the longest word in a list and counts the number of characters.

words = ['one','two','three','four','five']
longest = words[0]
for i in range(1,len(words),1):
    if len(words[i]) > len(longest):
        longest = words[i]
print ('longest word is', longest)
print('has',len(longest),'characters')

'''

/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 /Users/Brando/Library/Preferences/PyCharmCE2017.2/scratches/P38_FindTheLongestWord.py
longest word is three
has 5 characters

Process finished with exit code 0


'''