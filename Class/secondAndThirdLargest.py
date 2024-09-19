def secondAndThirdLargest(arr):
    max = arr[0]
    secondMax = arr[0]
    thirdMax = arr[0]
    for i in arr:
        if i >max:
            thirdMax = secondMax
            secondMax = max
            max = i

    return secondMax, thirdMax

a = [10,20,30,40,50,60,70,80,90,100]

print(secondAndThirdLargest(a))
