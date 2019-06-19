
go = True
while(go):
    sides = []
    angles = []
    print("Enter 4 sides of the shape.")
    sides.append(float(input("Side 1: ")))
    sides.append(float(input("Side 2: ")))
    sides.append(float(input("Side 3: ")))
    sides.append(float(input("Side 4: ")))

    print("Enter 4 angles of the shape.")
    angles.append(float(input("Angle 1: ")))
    angles.append(float(input("Angle 2: ")))
    angles.append(float(input("Angle 3: ")))
    angles.append(float(input("Angle 4: ")))

    #Program validates that it's a positive number
    #Program repeats if needed.

    for x in range(0,4,1):
        if(sides[x] < 0):
            print("Please enter a positive number for the ",x+1,'side.')
            sides[x] = input()
    for x in range(0,4,1):
        if(angles[x] < 0):
            print("Please enter a positive number for the ",x+1,'angle.')
            angles[x] = input()

    if(sides[0] == sides[1] and sides[1] == sides[2] and sides[2] == sides[3] and sides[3] == sides[0] and angles[0] == angles[2] and angles[1] == angles[3]and angles[0] != angles[1] and angles[2] != angles[3]):
        print("The shape is a Rhombus.")

    if(sides[0] == sides[1] and sides[1] == sides[2] and sides[2] == sides[3] and sides[3] == sides[0] and angles[0] == angles[1] and angles[1] == angles[2] and angles[2] == angles[3]):
        print("The shape is a Square.")

    if(angles[0] == angles[1] and angles[1] == angles[2] and angles[2] == angles[3] and angles[3] == angles[0] and sides[0] == sides[2] and sides[1] == sides[3] and sides[0] != sides[1] and sides[2] != sides[3]):
        print("The shape is a Rectangle.")

    decision = int(input("Would you like to repeat? 1=yes 2=no"))
    if(decision == 1):
        go = True
    elif(decision == 2):
        go = False


'''
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/MidtermLonger.py"
Enter 4 sides of the shape.
Side 1: 4
Side 2: 4
Side 3: 4
Side 4: 4
Enter 4 angles of the shape.
Angle 1: 1
Angle 2: 3
Angle 3: 1
Angle 4: 3
The shape is a Rhombus.
Would you like to repeat? 1=yes 2=no1
Enter 4 sides of the shape.
Side 1: 2
Side 2: 2
Side 3: 2
Side 4: 2
Enter 4 angles of the shape.
Angle 1: 3
Angle 2: 4
Angle 3: 3
Angle 4: 4
The shape is a Rhombus.
Would you like to repeat? 1=yes 2=no2

Process finished with exit code 0

/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/MidtermLonger.py"
Enter 4 sides of the shape.
Side 1: -4
Side 2: -3
Side 3: -2
Side 4: -1
Enter 4 angles of the shape.
Angle 1: 2
Angle 2: 2
Angle 3: 2
Angle 4: 2
Please enter a positive number for the  1 side.
4
Please enter a positive number for the  2 side.
3
Please enter a positive number for the  3 side.
4
Please enter a positive number for the  4 side.
3
The shape is a Rectangle.

Process finished with exit code 0

/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/MidtermLonger.py"
Enter 4 sides of the shape.
Side 1: 3
Side 2: 3
Side 3: 3
Side 4: 3
Enter 4 angles of the shape.
Angle 1: 1
Angle 2: 4
Angle 3: 1
Angle 4: 4
The shape is a Rhombus.

Process finished with exit code 0

/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/MidtermLonger.py"
Enter 4 sides of the shape.
Side 1: 4
Side 2: 4
Side 3: 4
Side 4: 4
Enter 4 angles of the shape.
Angle 1: 4
Angle 2: 4
Angle 3: 4
Angle 4: 4
The shape is a Square.

Process finished with exit code 0

/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/MidtermLonger.py"
Enter 4 sides of the shape.
Side 1: 2
Side 2: 3
Side 3: 2
Side 4: 3
Enter 4 angles of the shape.
Angle 1: 1
Angle 2: 1
Angle 3: 1
Angle 4: 1
The shape is a Rectangle.

Process finished with exit code 0
'''