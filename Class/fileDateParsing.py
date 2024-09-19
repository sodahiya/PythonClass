import re

f = open("mbox.txt", "r")
lines  = f.readlines()

format = "[0-9][0-9]:[0-9][0-9]:[0-9][0-9]"

for line in lines:
    if re.search(format, line) :
        print(line)