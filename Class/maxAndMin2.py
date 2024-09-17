a = float(input("Enter first number"))
b = float(input("Enter second number"))
c = float(input("Enter third number"))
d = float(input("Enter fourth number"))

if a>b:
    if a>c:
        if a>d:
            print("A",a,"is greatest")
        else:
            print("D",d,"is greatest")
    else:
        if c>d:
            print("C",c,"is greatest")
        else:
            print("D",d,"is greatest")
else:
    if b>c:
        if b>d:
            print("B",b,"is greatest")
        else:
            print("D",d,"is greatest")
    else:
        if c>d:
            print("C",c,"is greatest")
        else:
            print("D",d,"is greatest")


if a<b:
    if a<c:
        if a<d:
            print("A",a,"is smallest")
        else:
            print("D",d,"is smallest")
    else:
        if c<d:
            print("C",c,"is smallest")
        else:
            print("D",d,"is smallest")
else:
    if b<c:
        if b<d:
            print("B",b,"is smallest")
        else:
            print("D",d,"is smallest")
    else:
        if c<d:
            print("C",c,"is smallest")
        else:
            print("D",d,"is smallest")