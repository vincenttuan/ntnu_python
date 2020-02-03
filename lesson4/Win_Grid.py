import tkinter

win = tkinter.Tk()
win.title("Grid")

h_label = tkinter.Label(win, text='Height')
w_label = tkinter.Label(win, text='Weight')
h_entry = tkinter.Entry(win)
w_entry = tkinter.Entry(win)

h_label.grid(row=0, column=0)
h_entry.grid(row=0, column=1)

w_label.grid(row=1, column=0)
w_entry.grid(row=1, column=1)

button1 = tkinter.Button(win, text="計算 BMI")
button1.grid(row=2, column=1)

win.mainloop()