import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Chrome'
}

def getStock(symbol) :
    url = 'https://tw.stock.yahoo.com/q/ts?s=' + str(symbol)
    html = requests.get(url, headers=headers)

    sp = BeautifulSoup(html.text, 'html.parser')

    data = sp.find("td", text="13:30:00").find_parent("tr").find_all("td")

    dict = {}
    dict.setdefault('代號', symbol)
    dict.setdefault('時間', data[0].text.strip())
    dict.setdefault('買進', data[1].text.strip())
    dict.setdefault('賣出', data[2].text.strip())
    dict.setdefault('成交價', data[3].text.strip())
    dict.setdefault('漲跌', data[4].text.strip())
    dict.setdefault('張數', data[5].text.strip())
    return dict

list = []
for symbol in [2330, 2303, 2317, 3008, 2498] :
    dict = getStock(symbol)
    list.append(dict)
print(list)