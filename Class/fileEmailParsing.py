
f = open("mbox.txt", "r")
lines  = f.readlines()

format = "[0-9][0-9]:[0-9][0-9]:[0-9][0-9]"

for line in lines:
    try:
        atpos = line.find("@")
        if atpos == -1:
            continue
        ppos = line.rfind(" ", atpos)
        lpos = line.find(" ", atpos)
        print(line[ppos+1:lpos])
    except:
        continue