def maxOfaList(a):
    max = a[0]
    for i in range(1,len(a)):
        if a[i] > max:
            max = a[i]
    return max

a = [10,20,30,40,50,60,70,80,90,100]


print(maxOfaList(a))
