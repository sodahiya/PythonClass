inputlist = []
while True:
    line = input()
    if line == "End":
        break
    inputlist.append(line)

f = open("multipleLineWrite.txt", "w")
for line in inputlist:
    f.write(line + "\n")
f.close()