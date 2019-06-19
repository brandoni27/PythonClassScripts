# P25_CountingLetters.py
# Brandon Washington
# 5/21/2019
# Python 3.6
# Description: Class that counts letters in a sentence.



def count_chars(letter,txt):
    result = 0
    for char in txt:
        if(txt == letter):
            result += 1
        # same as result = result + 1
        return result


print(count_chars('e','Hello World'))