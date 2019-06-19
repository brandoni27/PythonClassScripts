# !through~.py
# Brandon Washington
# 2/27/2019
# Python 3.6
# Description: Program which prints a list of ASCII characters

from __future__ import print_function

count = 0
x = 33
list= []

while x<= 126:
    list.append(chr(x))
    if x % 10 == 1:
        print(*list[-10:], sep=' ')
    if x == 126:
        print(*list[-5:],sep=' ')
    x+=1


'''
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P18_!through~.py"
! " # $ % & ' ( )
* + , - . / 0 1 2 3
4 5 6 7 8 9 : ; < =
> ? @ A B C D E F G
H I J K L M N O P Q
R S T U V W X Y Z [
\ ] ^ _ ` a b c d e
f g h i j k l m n o
p q r s t u v w x y
z { | } ~

Process finished with exit code 0
'''