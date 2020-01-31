import json

x = {
        "name":"John",
        "height":170.5,
        "weight":60.5,
        "cars":[
            {"model":"toyota", "type":"PICKUP", "price":2500000},
            {"model":"porsche", "type":"911", "price":6500000}
        ]
    }

print(type(x))
# 請列出 cars, 並求資產總額
sum = 0
for car in x['cars']:
    print(car['model'], car['type'], car['price'])
    sum = sum + car['price']

print(sum)

y = json.dumps(x)
print(type(y))

