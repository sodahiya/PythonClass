def min(a,  b , c):
    if a < b:
        if a<c:
            return a
        else:
            return c
    else:
        if b<c:
            return b
        else:
            return c


a = float(input("Enter first number"))
b = float(input("Enter second number"))
c = float(input("Enter third number"))

print("The smallest number is ", min(a,b,c))

