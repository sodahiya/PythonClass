a =[2,4,3]
b = [5,6,4]

sum = 0
carry = 0
c = []
for i in range(len(a)):
    sum = a[i] + b[i]+ carry
    if sum>9:
        carry = 1
        sum %=10
    c.append(sum)
print(c)