import requests
from bs4 import BeautifulSoup

url = 'https://taqm.epa.gov.tw/pm25/tw/PM25A.aspx?area=10'

resp = requests.get(url)
html = resp.text
#print(html)

sp = BeautifulSoup(html, 'html.parser')

area = sp.find('a', {"id":"ctl08_gv_ctl20_linkSite"}).text.strip()
p1 = sp.find('span', {"id":"ctl08_gv_ctl20_lab1"}).text.strip()
p2 = sp.find('span', {"id":"ctl08_gv_ctl20_lab2"}).text.strip()
print(area, p1, p2)

print(sp.find('span', {"id":"ctl08_gv_ctl04_lab1"}).text.strip())

# 抓取所有資料
records = sp.find_all('tr', {"align":"center", "style":"border-width:1px;border-style:Solid;"})

for record in records:
    td = record.find_all('td')
    for i in range(0, 3):
        print(td[i].text.strip(), end=",")
    print('\n--------------------')
