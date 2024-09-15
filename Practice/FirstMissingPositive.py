nums = [3,4,-1,1]
nums.sort()

smallest = 1

for i in nums:
    if i < smallest:
        continue
    elif i == smallest:
        smallest += 1
    elif i != smallest:
        print (i)
print(smallest)