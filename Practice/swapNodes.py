lst = [1,2,3,4,5,6,7,8,9,10]
i = 0
while i < len(lst)-1:
    lst[i], lst[i+1] = lst[i+1],lst[i]

    i+=2
    print(lst)
print(lst)