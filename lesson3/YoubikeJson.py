import requests
import json

url = 'https://data.ntpc.gov.tw/od/data/api/54DDDC93-589C-4858-9C95-18B2046CC1FC?$format=json'

resp = requests.get(url)
if resp.status_code == 200:
    list = json.loads(resp.text)
    print(list)