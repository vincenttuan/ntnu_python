import json

x1 = '{"name":"John", "age":30}'
y1 = json.loads(x1) # 文字轉 json 物件
print(type(y1))
print(y1)
print(y1['name'])
print(y1['age'])

x2 = '[{"name":"John", "age":30},' \
     '{"name":"Mary", "age":20}]'

y2 = json.loads(x2)
print(type(y2))
print(y2)