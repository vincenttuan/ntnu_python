w = 60
h = 170
bmi = w / ((h/100)*(h/100))
print(bmi)
bmi = w / ((h/100)**2)
print(h, w, bmi)
print("身高:" + str(h) + " 體重:" + str(w) + " BMI:" + str(bmi))
print("身高: %d 體重: %d BMI: %.2f" % (h, w, bmi))
print("身高: %06d 體重: %06d BMI: %06.2f" % (h, w, bmi))
result = "身高: {0} 體重: {1} BMI: {2}".format(h, w, bmi)
print(result)
result = "身高: {0} 體重: {1} BMI: {2}".format(h, w, ("%.2f" % bmi))
print(result)