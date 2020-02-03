import random
import tkinter
from tkinter import messagebox

def calc():
    bmi = 0.0;
    messagebox.showinfo("你的 BMI 值 : ", str(bmi))


win = tkinter.Tk()
win.title("計算 BMI")

h_entry = tkinter.Entry(win, justify=tkinter.CENTER)
h_entry.config(font=('Arial', 40))
h_entry.insert(0, "170")
h_entry.pack()

w_entry = tkinter.Entry(win, justify=tkinter.CENTER)
w_entry.config(font=('Arial', 40))
w_entry.insert(0, "60")
w_entry.pack()

button1 = tkinter.Button(win, text="計算 BMI", command=calc)
button1.config(font=('Arial', 30))
button1.pack(side=tkinter.LEFT)

button2 = tkinter.Button(win, text="清空")
button2.config(font=('Arial', 30))
button2.pack(side=tkinter.RIGHT)


win.mainloop()




