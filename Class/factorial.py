def factorial(inp):
    for i in range(1,inp):
        inp *= i
    return inp

inp = int(input("Enter a number: "))

print(factorial(inp))
