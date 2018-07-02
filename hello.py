# -*- coding: UTF-8 -*-
from Tkinter import *


master = Tk()
var = IntVar()

def file_callback():
    print "file callback"
    print "variable is", var.get()

def oper_callback():
    print "oper callback"

def set_callback():
    print "set callback"

def help_callback():
    print "help callback"

class App:
    def __init__(self, master):
        fmTop = Frame(master, height=0, width=0)
        fmTop.pack_propagate(0)
        fmTop.pack()
        
        Button(master, text="文件", width=7, command=file_callback).pack(side=LEFT)
        Button(master, text="操作", width=7, command=oper_callback).pack(side=LEFT)
        Button(master, text="设置", width=7, command=set_callback).pack(side=LEFT)
        Button(master, text="帮助", width=7, command=help_callback).pack(side=LEFT)



#Checkbutton(master, text="操作", variable=var, command=callback).pack()

master.title("create bt scripe")
display = App(master)
master.mainloop()