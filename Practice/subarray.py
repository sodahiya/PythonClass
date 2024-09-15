a = [-2,1]
print(a)
max = 0
for i in range(len(a)):
    for j in range(i,len(a)+1):
        sum = 0
        for k in a[i:j]:
            sum += k
            if sum > max:
                print("Itteration is", a[i:j], "Sum is", sum)
                max = sum
print(max)