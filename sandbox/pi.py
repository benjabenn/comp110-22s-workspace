from random import random

total = 3141592
count = 0

for i in range(total):
    x = random()
    y = random()
    if x ** 2 + y ** 2 <= 1:
        count += 1

print("Pi is approximately " + str(4 * count / total))