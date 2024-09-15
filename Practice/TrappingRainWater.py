
height = [0,1,0,2,1,0,1,3,2,1,2,1]

maxLeft = 0
maxRight = 0
val = 0
sum = 0
for i in range(len(height)):
    if i>0:
        maxLeft = max(height[:i])
    else:
        maxLeft = 0
    if i<len(height)-1:
        maxRight = max(height[i+1:])
    else:
        maxRight = 0
    vol = min(maxLeft, maxRight) - height[i]
    if vol > 0 :
        sum += vol
print(sum)