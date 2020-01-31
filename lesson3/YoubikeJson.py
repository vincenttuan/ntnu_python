import requests
import json

url = 'https://data.ntpc.gov.tw/api/v1/rest/datastore/382000000A-000352-001'

resp = requests.get(url)
if resp.status_code == 200:
    jo = json.loads(resp.text)
    #print(jo)
    total = jo['result']['total']
    print('total: %d' % total)
    records = jo['result']['records']

    for record in records:
        # 請印出 sbi >= 30 and bemp >= 30 的站台
        n = 30
        sbi = int(record['sbi'])
        bemp = int(record['bemp'])
        if sbi >= n and bemp >= n:
            sna = record['sna']
            print(sna, sbi, bemp)




