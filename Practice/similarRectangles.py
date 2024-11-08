
a =[[2,1],[10,7],[9,6],[6,9],[7,3]]
count = 0
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if (a[i][0]/a[i][1]) == (a[j][0]/a[j][1]):
            count += 1
print(count)
