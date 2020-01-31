import json

def getData(y):
    name = y['name']
    h = y['height']
    w = y['weight']
    return name, h, w

x = '[{"name":"John", "height":170.5, "weight":60.5}, {"name":"Mary", "height":160.5, "weight":45.5}]'
list = json.loads(x)
print(type(list))

for y in list:
    value = getData(y)
    print(value)

    name, h, w = getData(y)
    print(name, h, w)

