import requests
import json

url = 'https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json'

resp = requests.get(url)
if resp.status_code == 200:
    jo = json.loads(resp.text)
    retVal = jo['retVal']
    for i in range(1, 405):
        no = '%04d' % i
        try:
            val = retVal[no]
            print(val['sna'], val)
        except:
            pass




