s = "a"
t = "a"

lst = []

for i in range(len(s)):
    for j in range(len(s)):
        if s[i:j] != "":
            lst.append(s[i:j+1])

lst.sort(key=lambda s: len(s))

print(lst)



for i in lst:
    flag = 0
    for j in t:
        if j not in i:
            flag = 1
    if flag == 0:
        print(i)





