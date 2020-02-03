import tkinter
import tkinter.messagebox

def show_askyesnocancel():
    r = tkinter.messagebox.askyesnocancel('對話框', 'This is [yesnocancel] dialog')
    print(r) # 按下 yes --> True, no --> False, cancel --> None

win = tkinter.Tk()
button1 = tkinter.Button(win, text="Click me", command=show_askyesnocancel)
button1.pack()
win.mainloop()


