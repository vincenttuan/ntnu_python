import requests
import json
import utils

def show_distance(record):
    # 師大緯經度 25.027243, 121.528459
    ntnu_lat = 25.027243
    ntnu_lng = 121.528459

    lat = float(record['lat'])
    lng = float(record['lng'])
    sna = record['sna']
    d = utils.distance(ntnu_lng, ntnu_lat, lng, lat)
    if d < 500:
        print(d, sna, record)


url = 'https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json'
resp = requests.get(url)
if resp.status_code == 200:
    jo = json.loads(resp.text)
    retVal = jo['retVal']

    for i in range(1, 405):
        no = '%04d' % i
        try:
            record = retVal[no]
            show_distance(record)
        except Exception as error:
            print(error)
            pass




