n =4
stri = "1"
for i in range(n-1):
    a = stri
    a = int(a[::-1])
    prev = None
    count = 1
    stri = ""
    while a > 0 :
        i = a % 10
        if i == prev:
            count += 1
        elif prev is not None:
            stri += str(count) + str(prev)
            count = 1
        prev = i
        a = a // 10
    stri += str(count) + str(prev)
    print(stri)