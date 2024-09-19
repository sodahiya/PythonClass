def fibonachi(n):
    a = 1
    b = 1
    fibo =[a]
    for i in range(n - 1):
        sum = a + b
        a = b
        b = sum
        fibo.append(a)
    return fibo

n = int(input("Enter a number: "))

print(fibonachi(n))
