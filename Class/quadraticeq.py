import math
a = int(input("Enter the coefficent of x^2 "))
b = int(input("Enter the coefficent of x "))
c = int(input("Enter the constant "))

d =  (b*b) - 4*(a*c)

if d >= 0 :
    print("Roots Are")
    print(((-b + math.sqrt(d))/(2*a)))
    print(((-b - math.sqrt(d))/(2*a)))
else :
    print("Imaginary roots")
