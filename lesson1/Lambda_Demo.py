def add(x, y):
    return x + y

print(add(10, 20))

g = lambda x, y : x + y
print(g(10, 20))

m = lambda x : x**2
print(m(3))

list_a = [lambda x : x**2, lambda x : x**3]
a = list_a[0]  # 相當於: a = lambda x : x**2
b = list_a[1]  # 相當於: b = lambda x : x**3
print(b(2))



