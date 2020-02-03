import random
import tkinter
from tkinter import messagebox

def get():
        messagebox.showinfo("Hello Python", entry.get())

def set():
    entry.delete(0, tkinter.END)
    entry.insert(0, str(random.randint(1, 100)))

win = tkinter.Tk()
entry = tkinter.Entry(win, justify=tkinter.CENTER)
entry.config(font=('Arial', 40))
entry.insert(0, '0')
entry.pack()

button1 = tkinter.Button(win, text="Get", command=get)
button1.config(font=('Arial', 30))
button1.pack(side=tkinter.LEFT)

button2 = tkinter.Button(win, text="Set", command=set)
button2.config(font=('Arial', 30))
button2.pack(side=tkinter.RIGHT)

win.mainloop()




