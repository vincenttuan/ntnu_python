import requests
import json

url = 'https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceFailure.aspx'

resp = requests.get(url)
if resp.status_code == 200:
    foods = json.loads(resp.text)
    print(foods)
    name = '冠軍'
    for food in foods:
        if food['品名'].find(name) >= 0:
            print('%s 不合格: %s' % (food['品名'], food['不合格原因']))
else:
    print('網路錯誤')