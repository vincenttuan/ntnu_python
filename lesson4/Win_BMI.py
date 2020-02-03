import tkinter
from tkinter import messagebox

def calc():
    try:
        h = float(h_entry.get())
        w = float(w_entry.get())
        bmi = w / (h/100)**2
    except Exception as e:
        messagebox.showinfo("錯誤", "資料輸入錯誤:" + str(e))
        return
    messagebox.showinfo("你的 BMI 值 : ", str("{0:.2f}".format(bmi)))


def clear():
    h_entry.delete(0, tkinter.END)
    w_entry.delete(0, tkinter.END)


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

button2 = tkinter.Button(win, text="清空", command=clear)
button2.config(font=('Arial', 30))
button2.pack(side=tkinter.RIGHT)


win.mainloop()




