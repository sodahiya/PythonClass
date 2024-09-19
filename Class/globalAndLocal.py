def sum(arg1, arg2):
    global total
    total = arg1 + arg2
    print("Inside the function local total : ", total)
    return total

print(sum(10, 20))