def area(side):
    try:
        side = float(side)
        print(side ** 2)
    except:
        print("Invalid number")


side = input("Enter square's length : ")
area(side)
