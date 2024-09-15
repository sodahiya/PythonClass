# This program prints the elements of a matrix in spiral order
matrix  = [   [ 1, 2, 3, 4 ],
		      [ 5, 6, 7, 8 ],
		      [ 9, 10, 11, 12 ],
	          [ 13, 14, 15, 16 ] ]

ans = []
r = len(matrix)
c = len(matrix[0])

top = 0
right = c-1
bottom = r-1
left = 0

while top <= bottom and left<= right:

    for i in range(left,right+1):
        ans.append(matrix[top][i])
    top +=1

    for i in range(top,bottom+1):
        ans.append(matrix[i][right])
    right -=1

    for i in range(right,left-1,-1):
        ans.append(matrix[bottom][i])
    bottom -=1

    for i in range(bottom,top-1 ,-1):
        ans.append(matrix[i][left])
    left +=1
print(ans)

print(matrix)