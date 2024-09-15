temperatures = (36.5, 37, 37.5, 38, 39)
F = list(map(lambda x: (float(9)/5)*x + 32, temperatures))
print(F)

a = [1,2,3,4]
b = [17,12,11,10]
c = [-1,-4,5,9]

print(list(map(lambda x,y:x+y, a,b)))
print(list(map(lambda x,y,z:x+y+z, a,b,c)))
