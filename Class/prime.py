a = input("Enter a number: ")

for i in range(2, int(a)):
    if int(a) % i == 0:
        print("Not a prime number")
        break
else:
    print("Prime number")