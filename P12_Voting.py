# Voting.py
# Brandon Washington
# 2/20/2019
# Python 3.6
# Description: Program which determines if I person can vote or not


# Take in the required information to determine if a person can vote.
age = int(input("How old are you?"))
citizenship = input("Are you a citizen? (y/n)?")
registered = input("Have you registered to vote? (y/n)?")

'''
If they meet all of the requirements, then they can vote. Otherwise,they cannot vote.
If they cannot vote, it will print the reason(s) why.
'''


if(age > 18 and citizenship == 'y' and registered == 'y'):
    print("Congratulations, you can vote!")

else:
    print("Sorry, you cannot vote.")
    if (age < 18):
        print("You are too young to vote.")
    if (citizenship == 'n'):
        print("You must be a citizen to vote.")
    if (registered == 'n'):
        print("You must be registered to vote.")


'''


/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P12_Voting.py"
How old are you?19
Are you a citizen? (y/n)?y
Have you registered to vote? (y/n)?y
Congratulations, you can vote!

Process finished with exit code 0


/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P12_Voting.py"
How old are you?1
Are you a citizen? (y/n)?y
Have you registered to vote? (y/n)?y
Sorry, you cannot vote.
You are too young to vote.

Process finished with exit code 0


/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P12_Voting.py"
How old are you?4
Are you a citizen? (y/n)?n
Have you registered to vote? (y/n)?y
Sorry, you cannot vote.
You are too young to vote.
You must be a citizen to vote.

Process finished with exit code 0


/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P12_Voting.py"
How old are you?6
Are you a citizen? (y/n)?n
Have you registered to vote? (y/n)?n
Sorry, you cannot vote.
You are too young to vote.
You must be a citizen to vote.
You must be registered to vote.

Process finished with exit code 0


'''