h = int(input('請輸入身高: ')) # str 轉 int
w = input('請輸入體重: ')
w = int(w) # str 轉 int
print(type(h))
print(type(w))
bmi = w / ((h/100)**2)
result = "身高: {0} 體重: {1} BMI: {2}".format(h, w, ("%.2f" % bmi))
print(result)