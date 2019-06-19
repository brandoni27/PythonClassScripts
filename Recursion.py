
def recursive(n):
    if n == 0:
        print("blastoff!")
    else:
        print(n)
        recursive(n-1)

recursive(50)