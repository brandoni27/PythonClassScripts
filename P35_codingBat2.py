# codingBat2.py
# Brandon Washington
# 5/11/2019
# Python 3.6
# Description: Multiple functions.

def cigar_party(cigars, is_weekend):
    if cigars < 40:
        return False
    if cigars >= 40 and cigars < 61:
        return True
    if cigars > 60 and is_weekend == False:
        return False
    if cigars >= 60 and is_weekend == True:
        return True




def count_evens(nums):
    evens = 0

    for num in nums:
        if num % 2 == 0:
            evens += 1

    return evens




def has22(nums):
  for i in range(len(nums)-1):
    if nums[i]==2 and nums[i+1]==2:
      return True
  else:
    return False



def sum67(nums):
  total = 0
  addNum = True
  for num in nums:
    if num == 6:
      addNum = False
    if addNum == True:
      total+=num
    if num == 7:
      addNum = True
  return total