# codingBat.py
# Brandon Washington
# 5/12/2019
# Python 3.6
# Description: Multiple string functions.

def string_times(str, n):
  string = str*n
  return string



def extra_end(str):
  string = str
  newString = string[-2:] *3
  return newString




def make_tags(tag, word):
  newTag = '<'+tag+'>'
  endTag = '</'+tag+'>'
  fullTag = newTag+word+endTag
  return fullTag


def combo_string(a, b):
    firstLength = len(a)
    secondLength = len(b)
    if firstLength < secondLength:
        return a + b + a
    elif secondLength < firstLength:
        return b + a + b

