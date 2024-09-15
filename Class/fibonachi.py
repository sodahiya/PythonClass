n = int(input("Enter a number: "))

a = 1
b = 1
print(a, end =  ',' )
for i in range(n-1):
    sum = a + b
    a = b
    b =sum
    print(a, end = ',')
