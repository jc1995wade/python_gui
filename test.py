# -*- coding: utf-8 -*-
from tkinter import *
root = Tk()

lb = Listbox(root,exportselection=False,height=3)
list_item=['1', '2', '3', '4这里很长我需要拽过来~~~~~~~~~~~~~~~','5','6','7']
for i in list_item:
    lb.insert(END,i)

scr1 = Scrollbar(root)
lb.configure(yscrollcommand = scr1.set)
scr1['command']=lb.yview
scr1.grid(row=5,column=4)

scr2 = Scrollbar(root,orient='horizontal')
lb.configure(xscrollcommand = scr2.set)
scr2['command']=lb.xview
scr2.grid(row=6,column=5)

scr3 = Scrollbar(root)
lb.configure(yscrollcommand = scr3.set)
scr3['command']=lb.yview
scr3.grid(row=5,column=6)

lb.grid(row=5,column=5)
root.mainloop()
