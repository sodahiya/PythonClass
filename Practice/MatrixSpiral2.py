n = 3
l = list(range(1, n*n+1))
print(l)
ans = [[0 for i in range(n)] for j in range(n)]
print(ans)
r = n
c = n
top = 0
right = c-1
bottom = r-1
left = 0

while top <= bottom and left<= right:

    for i in range(left,right+1):
        ans[top][i] = l.pop(0)
    top +=1

    for i in range(top,bottom+1):
        ans[i][right] = l.pop(0)
    right -=1

    for i in range(right,left-1,-1):
        ans[bottom][i] = l.pop(0)
    bottom -=1

    for i in range(bottom,top-1 ,-1):
        ans[i][left] = l.pop(0)
    left +=1
print(ans)