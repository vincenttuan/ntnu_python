import random
# 四星彩
def getNum(begin, end):
    num = random.randint(begin, end)
    return num;

for i in range(4):
    num = getNum(0, 9)
    print(i, num)


