import json

x = '{"name":"John", "height":170.5, "weight":60.5}'
y = json.loads(x)
print(type(y))
name = y['name']
h = y['height']
w = y['weight']
print(name, h, w)
