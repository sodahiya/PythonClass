from copy import deepcopy

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
matrix2 = deepcopy(matrix)


for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 0:
            for k in range(len(matrix)):
                matrix2[k][j] = 0
            for l in range(len(matrix[i])):
                matrix2[i][l] = 0

matrix = deepcopy(matrix2)
print(matrix)