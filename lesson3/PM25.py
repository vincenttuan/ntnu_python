import requests
from bs4 import BeautifulSoup

url = 'https://taqm.epa.gov.tw/pm25/tw/PM25A.aspx?area=10'

resp = requests.get(url)
html = resp.text
print(html)
