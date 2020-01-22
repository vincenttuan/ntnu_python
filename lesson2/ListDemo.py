import random

poker = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
print(poker)
# poker.reverse()
# print(poker)
# poker.sort()
# print(poker)
# 洗牌演算
for i in range(50):
    idx1 = random.randint(0, 12)
    idx2 = random.randint(0, 12)
    a = poker[idx1]
    b = poker[idx2]
    poker[idx1] = b
    poker[idx2] = a
print(poker)

# 洗牌演算 API
random.shuffle(poker)
print(poker)
