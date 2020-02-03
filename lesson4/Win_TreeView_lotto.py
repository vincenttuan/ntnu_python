import tkinter
import random
from tkinter import ttk  # 匯入資源

def addRecord():
    lottos = set()
    while len(lottos) < 5:
        lottos.add(random.randint(1, 39))

    tree.insert('', '0', values=list(lottos))  # end 最後一筆，0 第一筆
    tree.grid()
    win.after(10, addRecord)

win = tkinter.Tk()
tree = ttk.Treeview(win)  #表格

tree = ttk.Treeview(win, columns=['1','2','3','4','5'], show='headings')

tree.heading('1', text='n1')
tree.heading('2', text='n2')
tree.heading('3', text='n3')
tree.heading('4', text='n4')
tree.heading('5', text='n5')

tree.column('1',width=100, anchor='center')
tree.column('2',width=100, anchor='center')
tree.column('3',width=100, anchor='center')
tree.column('4',width=100, anchor='center')
tree.column('5',width=100, anchor='center')

win.after(1, addRecord)

tree.pack()
win.mainloop()
