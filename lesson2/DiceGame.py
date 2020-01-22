import random
dice = [1, 2, 3, 4, 5, 6]

def getDice():
    index = random.randint(0, 5)
    return dice[index]

def play(n):
    sum = 0
    for i in range(n):
        sum = sum + getDice()
    return sum

balance = 100
while True:
    bet = int(input('請加碼: '))
    if(bet > balance):
        continue

    input('請案任意鍵擲骰子(電腦)')
    pc_score = play(3)
    print('pc_score: %d' % pc_score)

    input('請案任意鍵擲骰子(玩家)')
    my_score = play(3)
    print('my_score: %d' % my_score)

    if my_score > pc_score:
        print('You Win YA~~')
        balance = balance + bet
    elif my_score < pc_score:
        print('你輸了')
        balance = balance - bet
    else:
        print('平手')

    print('balance: %d' % balance)

