# Astrology Program.py
# Brandon Washington
# 2/20/2019
# Python 3.6
# Description: Program which determines which Astrological sign you are and who you are compatible with.

# Holds the user's input for the days and months.
month = int(input("What month were you born in? "))
day = int(input("What day of the month were you born on? "))


# Logic for computing which sign they are based on their input.
if ( month == 3 and day >=21) or (month == 4 and day <= 19):
    print("You are Aries, The Ram, Fire group, compatible with Aries, Leo, Sagittarius")
if ( month == 4 and day >=20) or (month == 5 and day <= 20):
    print("You are Taurus, The Bull, Earth group, compatible with Taurus, Virgo, Capricorn")
if ( month == 5 and day >=21) or (month == 6 and day <= 21):
    print("You are Gemini, Air group, compatible with Gemini, Libra, Aquarius")
if ( month == 6 and day >=22) or (month == 7 and day <= 22):
    print("You are Cancer, Water group, compatible with Cancer, Scorpio, Pisces")
if ( month == 7 and day >=23) or (month == 8 and day <= 22):
    print("You are Leo, Fire group, compatible with Aries, Leo, Sagittarius")
if ( month == 8 and day >=23) or (month == 9 and day <= 22):
    print("You are Virgo, Earth group, compatible with Taurus, Virgo, Capricorn")
if ( month == 9 and day >=23) or (month == 10 and day <= 23):
    print("You are Libra, Air group, compatible with Gemini, Libra, Aquarius")
if ( month == 10 and day >=24) or (month == 11 and day <= 21):
    print("You are Scorpio, Water group, compatible with Cancer, Scorpio, Pisces")
if ( month == 11 and day >=22) or (month == 12 and day <= 21):
    print("You are Sagittarius, Fire group, compatible with Aries, Leo, Sagittarius")
if ( month == 12 and day >=22) or (month == 1 and day <= 19):
    print("You are Capricorn, Earth group, compatible with Taurus, Virgo, Capricorn")
if ( month == 1 and day >=20) or (month == 2 and day <= 18):
    print("You are Aquarius, Air group, compatible with Gemini, Libra, Aquarius")
if ( month == 2 and day >=19) or (month == 3 and day <= 20):
    print("You are Pisces, Water group, compatible with Cancer, Scorpio, Pisces")


'''
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P14_AstrologyProgram.py"
What month were you born in? 10
What day of the month were you born on? 27
You are Scorpio, Water group, compatible with Cancer, Scorpio, Pisces

Process finished with exit code 0



/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P14_AstrologyProgram.py"
What month were you born in? 3
What day of the month were you born on? 22
You are Aries, The Ram, Fire group, compatible with Aries, Leo, Sagittarius

Process finished with exit code 0



/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P14_AstrologyProgram.py"
What month were you born in? 1
What day of the month were you born on? 21
You are Aquarius, Air group, compatible with Gemini, Libra, Aquarius

Process finished with exit code 0



/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P14_AstrologyProgram.py"
What month were you born in? 4
What day of the month were you born on? 21
You are Taurus, The Bull, Earth group, compatible with Taurus, Virgo, Capricorn

Process finished with exit code 0

'''