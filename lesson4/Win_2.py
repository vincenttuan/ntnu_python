import tkinter
from datetime import datetime

win = tkinter.Tk()
# 視窗抬頭
win.title("我的視窗")
# 視窗大小
win.geometry("600x600")
# 放入 Label
label = tkinter.Label(win, text=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), bg='green', fg='yellow')
label.config(font=('Arial', 40))
#label = tkinter.Label(win, text="Hello")
label.pack(side=tkinter.TOP)

win.mainloop()


