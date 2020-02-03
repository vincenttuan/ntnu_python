import tkinter

win = tkinter.Tk()
win.title("Grid")

btn1 = tkinter.Button(text='btn1', font=('Arial', 36))
btn2 = tkinter.Button(text='btn2', font=('Arial', 36))
btn3 = tkinter.Button(text='btn3', font=('Arial', 36))
btn4 = tkinter.Button(text='btn4', font=('Arial', 36))

win.rowconfigure((0, 1), weight=1)  # 列 0, 列 1 同步放大縮小
win.columnconfigure((0, 1, 2), weight=1)  # 欄 0, 欄 1, 欄 2 同步放大縮小

btn1.grid(row=0, column=0, rowspan=2, sticky='EWNS') # sticky='EWNS' 無縫填滿
btn2.grid(row=0, column=1, columnspan=2, sticky='EWNS')
btn3.grid(row=1, column=1, columnspan=1, sticky='EWNS')
btn4.grid(row=1, column=2, columnspan=1, sticky='EWNS')

win.mainloop()