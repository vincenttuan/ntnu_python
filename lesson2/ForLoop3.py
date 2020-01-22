employees = {
    'Tom':[70000, 1, {'m':2.5}],
    'Mary':[80000, 2, {'m':1.5}],
    'John':[55000, 2, {'m':3}],
}
for key in employees:
    print('%s 的資料 %s' % (key, employees[key]))
print('---------------------------------------------')
for key in employees:
    if(employees[key][1] == 2) :
        print('%s 的資料 %s' % (key, employees[key]))
print('---------------------------------------------')
for key in employees:
    m = employees[key][2]['m']
    print('%s 的資料 %s' % (key, employees[key][0] * m))
print('---------------------------------------------')
# max 是誰 ?
maxValue = 0
for i in [10, 30, 20]:
    if i > maxValue:
        maxValue = i
print('maxValue: %d' % maxValue)
print('---------------------------------------------')
# max 是誰 ?
maxName, maxSalary = '', 0
for key in employees:
    m = employees[key][2]['m']
    salary = employees[key][0] * m
    if salary > maxSalary:
        maxName = key
        maxSalary = salary

print('maxName: %s maxSalary: %d' % (maxName, maxSalary))
