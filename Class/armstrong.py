a = int(input("Enter a integer number: "))

def count_digits(n0):
    count = 0
    while n0 > 0:
        count += 1
        n0 = n0 // 10
    return count
b = a
sum = 0
n = count_digits(a)
while a > 0:
    digit = a % 10
    sum += digit ** n
    a = a // 10
if sum == b:
    print("Armstrong number")
else:
    print("Not an Armstrong number")