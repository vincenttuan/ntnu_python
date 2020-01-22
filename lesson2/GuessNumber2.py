import random

begin, end, count = 0, 100, 5
ans = random.randint(begin+1, end-1)


def check(iGuess, iBegin, iEnd):
    if iGuess == ans:
        return True, iBegin, iEnd
    elif guess < ans:
        return False, guess, iEnd
    else:
        return False, iBegin, guess


while 1:
    guess = int(input('第 %d 次: 請在 %d ~ %d 間輸入數字: ' % (count, begin, end)))

    if guess <= begin or guess >= end:
        print('數字範圍錯誤')
        continue

    result, begin, end = check(guess, begin, end)
    if result:
        print('答對了')
        break;

    count = count - 1;
    if count == 0:
        print('次數用完, 答案是: %d' % ans)
        break;
