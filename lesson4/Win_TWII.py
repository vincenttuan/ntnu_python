import tkinter
from datetime import datetime
import requests
from bs4 import BeautifulSoup

def update_twii():
    url = 'https://tw.stock.yahoo.com/'
    resp = requests.get(url)
    html = resp.text
    #print(html)
    '''
    <td class="dx">11349.49</td>
    <td class="im"><span class="downi"><i>跌</i></span></td>
    <td class="chg down">145.61</td>
    <td class="vol"><span>1107.55億</span></td>
    '''
    sp = BeautifulSoup(html, 'html.parser')
    dx = sp.find("td", {"class": "dx"})
    im = sp.find("td", {"class": "im"})
    cd = sp.find("td", {"class": "chg down"})
    vl = sp.find("td", {"class": "vol"})
    dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    print(dx.text, im.text, cd.text, vl.text)

    dx_var.set(dx.text)
    if cd.text.strip() == '0':
        cd_var.set(cd.text)
        cd_label.config(fg="black")
    else:
        if im.text.strip() == '跌':
            cd_var.set('-' + cd.text)
            cd_label.config(fg="green")
        else:
            cd_var.set(cd.text)
            cd_label.config(fg="red")

    vl_var.set(vl.text)
    dt_var.set(dt)
    win.after(1000, update_twii)

win = tkinter.Tk()
# 視窗抬頭
win.title("台灣加權股價指數")
# 視窗大小
win.geometry("500x250")
# 放入 Label
dx_var = tkinter.StringVar()
cd_var = tkinter.StringVar()
vl_var = tkinter.StringVar()
dt_var = tkinter.StringVar()

dx_label = tkinter.Label(win, textvariable=dx_var, font=('Arial', 40))
cd_label = tkinter.Label(win, textvariable=cd_var, font=('Arial', 30))
vl_label = tkinter.Label(win, textvariable=vl_var, font=('Arial', 30))
dt_label = tkinter.Label(win, textvariable=dt_var, font=('Arial', 20))

dx_label.pack()
cd_label.pack()
vl_label.pack()
dt_label.pack()

win.after(1, update_twii)
win.mainloop()


