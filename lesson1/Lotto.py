import random
# 四星彩
a = random.randint(0, 9)
b = random.randint(0, 9)
c = random.randint(0, 9)
d = random.randint(0, 9)
print(a, b, c, d)

for i in range(4):
    num = random.randint(0, 9)
    print(i, num)

r1 = range(4)
for i in r1:
    num = random.randint(0, 9)
    print(i, num)

