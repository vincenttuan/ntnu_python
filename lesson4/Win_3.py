import tkinter
import random

num = 0;

def update_number():
    global num
    num = num + 1
    print(str(num))
    var.set(str(num))

def update_lotto():
    lottos = set()
    while len(lottos) < 5:
        lottos.add(random.randint(1, 39))

    print(tuple(lottos))
    var.set(tuple(lottos))

win = tkinter.Tk()
# 視窗抬頭
win.title("我的視窗")
# 視窗大小
win.geometry("600x600")
# 字串參照物件
var = tkinter.StringVar()
# 放入 Label
label = tkinter.Label(win, textvariable=var, bg='green', fg='yellow')
label.config(font=('Arial', 40))
label.pack(side=tkinter.TOP)

button1 = tkinter.Button(win, text="GetNumber", font=('Arial', 20), command=update_number)
button1.pack(side=tkinter.LEFT)

button2 = tkinter.Button(win, text="539", font=('Arial', 20), command=update_lotto)
button2.pack(side=tkinter.RIGHT)

win.mainloop()




