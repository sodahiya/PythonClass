a = float(input("Enter first number"))
b = float(input("Enter second number"))
c = float(input("Enter third number"))


if a > b:
    if a>c:
        print("A",a,"is greatest")
    else:
        print("C",c,"is greatest")
else:
    if b>c:
        print("B",b,"is greatest")
    else:
        print("C",c,"is greatest")

if a<b:
    if a<c:
        print("A",a,"is smallest")
    else:
        print("C",c,"is smallest")
else:
    if b<c:
        print("B",b,"is smallest")
    else:
        print("C",c,"is smallest")