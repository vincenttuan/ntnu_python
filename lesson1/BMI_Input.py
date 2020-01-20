h = int(input('請輸入身高: ')) # str 轉 int
w = input('請輸入體重: ')
w = int(w) # str 轉 int
print(type(h))
print(type(w))
bmi = w / ((h/100)**2)
result = "身高: {0} 體重: {1} BMI: {2}".format(h, w, ("%.2f" % bmi))
print(result)

info = '正常'
if bmi > 23:
    print('過重')
    info = '過重'
elif bmi < 18:
    print('過輕')
    info = '過輕'
else:
    print('正常')

result = "身高: {0} 體重: {1} BMI: {2} {3}".format(h, w, ("%.2f" % bmi), info)
print(result)