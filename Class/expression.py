a = float(input("Enter first number"))
b = float(input("Enter second number"))
c = float(input("Enter third number"))
d = float(input("Enter fourth number"))

r = (a+ b) * c / d

print("Result is ", r)

r = a+ b * c / d

print("Result is ", r)

# The difference in result is due to the precedence of operators. In the first case, the addition operator has higher
# precedence than the multiplication and division operators. In the second case, the multiplication and division operators
# have higher precedence than the addition operator. This leads to different results in the two cases.