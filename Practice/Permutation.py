import itertools
n =4
k =9
l = list(range(1,n+1))
print(l)
l = list(itertools.permutations(l))
s = ""
for i in l[k-1]:
    s += str(i)
print(s)
