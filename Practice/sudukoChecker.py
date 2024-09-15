from copy import deepcopy

def transpose(X):
    result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]
    return result

def check(X):
    for i in X:
        i.sort()
        for j in range(0, len(i) - 1):
            if i[j] == ".":
                continue
            elif int(i[j])> 9 or int(i[j]) < 1:
                return False
            elif i[j] == i[j + 1]:
                return False
    return True
def check2(X):
    X.sort()
    for i in range(0,len(X)-1):
        if X[i] ==".":
            continue
        elif int(X[i]) > 9 or int(X[i]) < 1:
            return False
        elif X[i] == X[i+1]:
            return False
    return True



a = [[".",".",".",".","5",".",".","1","."],
     [".","4",".","3",".",".",".",".","."],
     [".",".",".",".",".","3",".",".","1"],
     ["8",".",".",".",".",".",".","2","."],
     [".",".","2",".","7",".",".",".","."],
     [".","1","5",".",".",".",".",".","."],
     [".",".",".",".",".","2",".",".","."],
     [".","2",".","9",".",".",".",".","."],
     [".",".","4",".",".",".",".",".","."]]

b = deepcopy(a)
b.sort()
t = transpose(a)
t.sort()

print(check(b))
print(check(t))

arr1,arr2,arr3,arr4,arr5,arr6,arr7,arr8,arr9 = [],[],[],[],[],[],[],[],[]
arr1.append(a[0][0:3] + a[1][0:3] + a[2][0:3])
arr2.append(a[0][3:6] + a[1][3:6] + a[2][3:6])
arr3.append(a[0][6:9] + a[1][6:9] + a[2][6:9])
arr4.append(a[3][0:3] + a[4][0:3] + a[5][0:3])
arr5.append(a[3][3:6] + a[4][3:6] + a[5][3:6])
arr6.append(a[3][6:9] + a[4][6:9] + a[5][6:9])
arr7.append(a[6][0:3] + a[7][0:3] + a[8][0:3])
arr8.append(a[6][3:6] + a[7][3:6] + a[8][3:6])
arr9.append(a[6][6:9] + a[7][6:9] + a[8][6:9])

arr1 = [j for sub in arr1 for j in sub]
arr2 = [j for sub in arr2 for j in sub]
arr3 = [j for sub in arr3 for j in sub]
arr4 = [j for sub in arr4 for j in sub]
arr5 = [j for sub in arr5 for j in sub]
arr6 = [j for sub in arr6 for j in sub]
arr7 = [j for sub in arr7 for j in sub]
arr8 = [j for sub in arr8 for j in sub]
arr9 = [j for sub in arr9 for j in sub]


if(check2(arr1) and check2(arr2) and check2(arr3) and check2(arr4) and check2(arr5) and check2(arr6) and check2(arr7) and check2(arr8) and check2(arr9)):
    print("True")
else:
    print("False")
