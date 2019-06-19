# classAssignment.py
# Brandon Washington
# 5/21/2019
# Python 3.6
# Description: Class about dates.



class Date:
    def __init__(self):
        self.month = 0
        self.day = 0
        self.year = 0
    def setDate(self,m,d,y):
        self.month = m
        self.day = d
        self.year = y
    def showDate(self):
        month = self.month
        day = self.day
        year = self.year
        print(month,'/',day,'/',year)

x = Date
x.setDate(Date,12,3,2003)
x.showDate(Date)

'''
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 /Users/Brando/Library/Preferences/PyCharmCE2017.2/scratches/scratch_5.py
12 / 3 / 2003

Process finished with exit code 0
'''