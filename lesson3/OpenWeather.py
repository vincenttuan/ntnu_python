import requests
import json

url = 'https://openweathermap.org/data/2.5/weather?q=Taipei&appid=b6907d289e10d714a6e88b30761fae22'

resp = requests.get(url)
if resp.status_code == 200:
    jo = json.loads(resp.text)
    main = jo['main']
    print('溫度:', main['temp'], '°C')
    print('體感:', main['feels_like'], '°C')
    print('濕度:', main['humidity'], '%')
