def check(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
a = int(input("Enter year"))
print(a," is a leap year") if check(a) else print(a," is not a leap year")

