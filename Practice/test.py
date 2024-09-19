def checkByPass(anum,astr,atup,alist):
    print(id(anum),id(astr),id(astr),id(alist))
    anum +=1
    astr+= astr
    alist[1] = '$'

    print(anum,astr,atup,alist)
    print(id(anum),id(astr),id(astr),id(alist))


anum = 5
bnum = 5

astr = "banana"

atup = tuple(astr)

alist = list("banana")
bstr = list("banana")


checkByPass(anum,astr,atup,alist)
