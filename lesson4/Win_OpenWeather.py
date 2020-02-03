import tkinter
import tkinter.font as tkFont
import requests
import json
import urllib.request
from io import BytesIO
from PIL import Image, ImageTk

def ok_cmd():
    print('ok_cmd')
    url = 'https://openweathermap.org/data/2.5/weather?q=Taipei&appid=b6907d289e10d714a6e88b30761fae22'
    resp = requests.get(url)
    if resp.status_code == 200:
        jo = json.loads(resp.text)
        main = jo['main']
        icon = jo['weather'][0]['icon']
        img_url = 'http://openweathermap.org/img/wn/%s.png' % icon
        value = '溫度：{0:.2f}°C\n體感：{1:.2f}°C\n濕度：{2:.2f}%'.format(main['temp'], main['feels_like'], main['humidity']);
        var.set(value)

        raw_data = urllib.request.urlopen(img_url).read()
        im = Image.open(BytesIO(raw_data)).resize((80, 80), Image.ANTIALIAS)

        photo = ImageTk.PhotoImage(im)
        label_img.configure(image=photo)
        label_img.image = photo

        print('溫度:', main['temp'], '°C')
        print('體感:', main['feels_like'], '°C')
        print('濕度:', main['humidity'], '%')
        print('icon:', icon)
        print('url:', img_url)

def cancel_cmd():
    print('cancel_cmd')
    win.quit()


win = tkinter.Tk()
win.title("OpenWeather")
win.geometry("300x300")
var = tkinter.StringVar() # 字串參照物件
fontStyle = tkinter.font.Font(family="Arial", size=20)
label = tkinter.Label(win, textvariable=var, font=fontStyle)
label.pack()

label_img = tkinter.Label(win, image=None)
label_img.pack()

button1 = tkinter.Button(win, text="天氣", font=fontStyle, command=ok_cmd)
button1.pack(side=tkinter.LEFT)

button2 = tkinter.Button(win, text="離開", font=fontStyle, command=cancel_cmd)
button2.pack(side=tkinter.RIGHT)

win.mainloop()
