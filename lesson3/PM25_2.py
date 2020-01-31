import requests
from bs4 import BeautifulSoup

url = 'https://taqm.epa.gov.tw/pm25/tw/PM25A.aspx?area=10'

resp = requests.get(url)
html = resp.text

sp = BeautifulSoup(html, 'html.parser')

# 抓取所有 PM2.5 資料
records = sp.find_all('tr', {"align":"center", "style":"border-width:1px;border-style:Solid;"})

# 將資料匯入 list[]
list = []
for record in records:
    td = record.find_all('td')
    dict = {}
    dict.setdefault("area", td[0].text.strip())
    dict.setdefault("p1", td[1].text.strip())
    dict.setdefault("p2", td[2].text.strip())
    list.append(dict)

print(list)
list_sorted = sorted(list, key=lambda dict: dict["p1"], reverse=True)
print(list_sorted)
max = max(list, key=lambda dict: dict["p1"])
print(max)

#f = open("pm25.csv", "a", encoding='UTF-8')
f = open("pm25.csv", "a")
f.write("area,p1,p2\n")
for dict in list:
    f.write(dict['area'] + "," + dict['p1'] + "," + dict['p2'] + "\n")




