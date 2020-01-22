import random
#import os
dice = [1, 2, 3, 4, 5, 6]

def getDice():
    index = random.randint(0, 5)
    print(dice[index])
    return dice[index]

def play(n):
    sum = 0
    for i in range(n):
        sum = sum + getDice()
    return sum

score = play(3)
print('score: %d' % score)
#os.system('cls')

