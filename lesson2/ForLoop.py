r = range(0, 5)
r2 = range(0, 10)
for i in r2:
    print(i, 'Python')

for item in [10, 20, 30, 40, 50]:
    print(item)

scores = [100, 80, 90]
sum = 0
for score in scores:
    sum = sum + score
    print(score)

print('sum: %d avg: %d' % (sum, sum/len(scores)))