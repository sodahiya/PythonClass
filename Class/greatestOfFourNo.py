a = float(input("Enter first number"))
b = float(input("Enter second number"))
c = float(input("Enter third number"))
d = float(input("Enter fourth number"))

if a > b:
    if a > c:
        if a > d:
            print("A is greatest")
        else:
            print("D is greatest")
    else:
        if c > d:
            print("C is greatest")
        else:
            print("D is greatest")
elif b > a:
    if b > c:
        if b > d:
            print("B is greatest")
        else:
            print("D is greatest")
    else:
        if c > d:
            print("C is greatest")
        else:
            print("D is greatest")