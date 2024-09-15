words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
largerlst = []
lst = list()
count = 0
for i in words:
    count += len(i)
    if count < maxWidth:
        lst.append(i)
    else:
        largerlst.append(lst)
        count = len(i)
        lst = lst[:0]
        lst.append(i)
    count += 1
    print("Count after",i,"is",count)
largerlst.append(lst)
print(largerlst)
final = list()

for i in largerlst:
    count = 0
    for j in i:
        count+= len(j)

    str = ""

    for j in i:
        str += j
        if j != i[-1]:
            for k in range((maxWidth - count) // (len(i) - 1)):
                str += " "
    print(str)
    final.append(str)
print(final)