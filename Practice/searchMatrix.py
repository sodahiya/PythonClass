matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

for i in matrix:
    for j in i:
        if j == target:
            print(True)
            break
