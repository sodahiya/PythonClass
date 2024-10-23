import re
f = open("mbox.txt")

lines  = f.readlines()

emails = {}

for line in lines:
    try:
        em = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", line)[0]
        if em != []:
            print(em)
            if em not in emails:
                emails.update({em:1})
            else:
                emails[em] += 1
    except:
        continue
print(emails)
