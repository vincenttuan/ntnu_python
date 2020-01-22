import random

begin = 0
end = 100
count = 5

ans = random.randint(begin+1, end-1)

while 1:
    guess = int(input('第 %d 次: 請在 %d ~ %d 間輸入數字: ' % (count, begin, end)))

    if guess <= begin or guess >= end:
        print('數字範圍錯誤')
        continue

    if guess == ans:
        print('答對了')
        break
    elif guess < ans:
        begin = guess
    else:
        end = guess

    count = count - 1;
    if count == 0:
        print('次數用完, 答案是: %d' % ans)
        break;
