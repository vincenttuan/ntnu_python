names = ['John', 'Mary', 'Tom']
for name in names:
    print(names.index(name), name)

if 'Tom' in names:
    print('Yes')
else:
    print('None')

employees = {'Tom':70000, 'Mary':80000, 'John':55000}
for key in employees:
    print('%s 的薪資 %d' % (key, employees[key]))