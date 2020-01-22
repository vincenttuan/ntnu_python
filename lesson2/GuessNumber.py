import random

begin = 0
end = 100
ans = random.randint(begin+1, end-1)

while 1:
    guess = int(input('請在 %d ~ %d 間輸入數字: ' % (begin, end)))
    if guess == ans:
        print('答對了')
        break
    elif guess < ans:
        begin = guess
    else:
        end = guess
