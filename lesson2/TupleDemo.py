import random
money = (500, 2000, 8000, 20000, 50000)
nums = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13]
random.shuffle(nums)
nums = tuple(nums)
#print(nums)

for i in range(5):
    code = int(input('比 7 大按 1, 小按 0 : '))
    if code == 1:
        if nums[i] > 7:
            print('%d : 過第 %d 關 獎金: %d' % (nums[i], (i+1), money[i]))
        else:
            print('%d : 闖關失敗, nums: %s' % (nums[i], nums))
            break
    elif code == 0:
        if nums[i] < 7:
            print('%d : 過第 %d 關 獎金: %d' % (nums[i], (i+1), money[i]))
        else:
            print('%d : 闖關失敗, nums: %s' % (nums[i], nums))
            break




