import random

count = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0}

for i in range(1000):
    dice = random.randint(1, 6)
    count[str(dice)] += 1

print(count)