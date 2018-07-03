# -*- coding: UTF-8 -*-
from Tkinter import *
from distutils import command


master = Tk()
master.geometry("600x400+300+100")#窗口大小，位置
var = IntVar()

def newfile_callback():
    print "new file"

def openfile_callback():
    print "open file"

def savefile_callback():
    print "save file"
    
def save_as_callback():
    print "save as file"

#在大窗口下定义一个菜单实例
menubar = Menu(master)

#为每个菜单实例添加菜单项
fmenu = Menu(menubar, tearoff=0)

#添加菜单按钮
fmenu.add_command(label='新建文件', command=newfile_callback)
fmenu.add_command(label='打开文件', command=openfile_callback)
fmenu.add_command(label='保存',     command=savefile_callback)
fmenu.add_command(label='另存为',   command=save_as_callback)


vmenu = Menu(menubar, tearoff=0)
for each in ['添加按键功能']:
    vmenu.add_command(label=each)

smenu = Menu(menubar, tearoff=0)
for each in ['设置']:
    smenu.add_command(label=each)

hmenu = Menu(menubar, tearoff=0)
for each in ['帮助', '关于']:
    hmenu.add_command(label=each)


def file_callback():
    print "file callback"
    #print "variable is", var.get()
#为顶级菜单实例添加菜单，并级联相应的子菜单实例    
menubar.add_cascade(label='文件', menu=fmenu)
menubar.add_cascade(label='操作', menu=vmenu)
menubar.add_cascade(label='设置', menu=smenu)
menubar.add_cascade(label='帮助', menu=hmenu)






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
        
        #Button(master, text="文件", width=7, command=file_callback).pack(side=LEFT)
        #Button(master, text="操作", width=7, command=oper_callback).pack(side=LEFT)
        #Button(master, text="设置", width=7, command=set_callback).pack(side=LEFT)
        #Button(master, text="帮助", width=7, command=help_callback).pack(side=LEFT)



#Checkbutton(master, text="操作", variable=var, command=callback).pack()

master['menu']=menubar
master.title("create bt scripe")
display = App(master)
master.mainloop()