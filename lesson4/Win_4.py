import tkinter
from datetime import datetime

def update_time():
    dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(dt)
    var.set(dt)
    win.after(1000, update_time)

win = tkinter.Tk()
# 視窗抬頭
win.title("我的視窗")
# 視窗大小
win.geometry("600x600")
# 放入 Label
var = tkinter.StringVar()
label = tkinter.Label(win, textvariable=var, bg='green', fg='yellow')
label.config(font=('Arial', 40))
#label = tkinter.Label(win, text="Hello")
label.pack(side=tkinter.TOP)

win.after(1, update_time)
win.mainloop()


