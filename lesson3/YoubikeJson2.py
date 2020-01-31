import requests
import json


def show(n, record):
    sbi = int(record['sbi'])
    bemp = int(record['bemp'])
    if sbi >= n and bemp >= n:
        sna = record['sna']
        print(sna, sbi, bemp)


url = 'https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json'
resp = requests.get(url)
if resp.status_code == 200:
    jo = json.loads(resp.text)
    retVal = jo['retVal']
    for i in range(1, 405):
        no = '%04d' % i
        try:
            record = retVal[no]
            #print(record['sna'], record)
            show(30, record)
        except Exception as error:
            print(error)
            pass

