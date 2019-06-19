# groceryBag.py
# Brandon Washington
# 5/21/2019
# Python 3.6
# Description: Class with grocery bags.


class Item:
    numberOfItems = 0

    def __init__(self, name, cost):
        self.itemName = name
        self.itemCost = cost
        Item.numberOfItems += 1

    def show(self):
        print(self.itemName,self.itemCost)
    def getName(self):
        return self.itemName
    def getCost(self):
        return self.itemCost
    def setName(self,n):
        self.itemName = n
    def setCost(self,c):
        self.itemCost = c

eggs = Item('Eggs',2.99)
bacon = Item('Bacon',4.99)
water = Item('Water',3.99)
bread = Item('Bread',2.59)
juice = Item('Juice',1.99)
coffee = Item('Coffee', 2.50)
groceryBag = []
groceryBag.append(eggs)
groceryBag.append(bacon)
groceryBag.append(water)
groceryBag.append(bread)
groceryBag.append(juice)
groceryBag.append(coffee)
print(Item.numberOfItems, 'items were purchased.')
total = 0
for food in groceryBag:
    total += Item.getCost(food)
print("The total is",total)

'''
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 /Users/Brando/Library/Preferences/PyCharmCE2017.2/scratches/scratch_7.py
6 items were purchased.
The total is 19.05

Process finished with exit code 0
'''