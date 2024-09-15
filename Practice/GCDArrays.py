a = int( input())
arr =[]
for i in range(0, a):
    l,r,k = map(int, input(). split())
    arr = list(range(l, r + 1))
    while len(arr) > 1 :
        x = arr[0]
        y = arr[1]
        arr.pop(0)
        arr[0] = x * y
        print(str(arr))    