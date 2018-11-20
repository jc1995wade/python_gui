# -*- coding: UTF-8 -*-
from Tkinter import *
from distutils import command
from tkinter import messagebox
import tkinter.font as tkFont

master = Tk()
master.geometry("580x400+300+100")#窗口大小，位置



def print_button(master):
    btnSelect = Button(master, text="Select", width=7, height=1, command=file_callback)
    btnSelect.place(x=500, y=10, anchor = 'nw')

    btnSelect = Button(master, text="Refresh", width=7, height=1, command=file_callback)
    btnSelect.place(x=500, y=50, anchor = 'nw')

    btnSelect = Button(master, text="SaveFile", width=7, height=1, command=file_callback)
    btnSelect.place(x=500, y=90, anchor = 'nw')



def print_text(master):
    #打印文本框
    testFont = tkFont.Font(family='Fixdsys', size=12)
    textFile = Text(master, width=50, height=1, font=testFont)
    textFile.place(x=80, y=10, anchor='nw')
    textFile.insert(INSERT,'Please select file')

    textOTA = Text(master, width=50, height=1, font=testFont)
    textOTA.place(x=80, y=50, anchor='nw')

    textInfact = Text(master, width=50, height=1, font=testFont)
    textInfact.place(x=80, y=90, anchor='nw')

    textFact = Text(master, width=50, height=1, font=testFont)
    textFact.place(x=80, y=130, anchor='nw')

    textItem = Text(master, width=8, height=1, font=testFont)
    textItem.place(x=80, y=200, anchor='nw')

    textVersion = Text(master, width=15, height=1, font=testFont)
    textVersion.place(x=230, y=200, anchor='nw')

    textTime = Text(master, width=15, height=1, font=testFont)
    textTime.place(x=420, y=200, anchor='nw')

    textCompany = Text(master, width=15, height=1, font=testFont)
    textCompany.place(x=80, y=240, anchor='nw')

    textProject = Text(master, width=20, height=1, font=testFont)
    textProject.place(x=280, y=240, anchor='nw')

    textMessage = Text(master, width=58, height=6, font=testFont)
    textMessage.place(x=80, y=280, anchor='nw')
    textMessage.insert(INSERT, 'hello world\n')
    textMessage.insert(INSERT, 'hello world')


def print_lable(master):
    #打印标签
    labFile = Label(master, text="File Path:")
    labFile.place(x=10, y=10, anchor='nw')

    labOTA = Label(master, text="OTA:")
    labOTA.place(x=10, y=50, anchor='nw')

    labInfact = Label(master, text="INFACT:")
    labInfact.place(x=10, y=90, anchor='nw')

    labFact = Label(master, text="FACT:")
    labFact.place(x=10, y=130, anchor='nw')


    labItem    = Label(master, text="Item:").place(x=10, y=200, anchor='nw')
    labVersion = Label(master, text="Version:").place(x=170, y=200, anchor='nw')
    labTime    = Label(master, text="Time:").place(x=370, y=200, anchor='nw')
    labCompany = Label(master, text="Company:").place(x=10, y=240, anchor='nw')
    labProject = Label(master, text="Project:").place(x=220, y=240, anchor='nw')
    labMessage = Label(master, text="Message:").place(x=10, y=280, anchor='nw')

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
    messagebox.showinfo('复制', '编辑-复制！')  # 消息提示框


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

        #lable
        print_lable(master)
        print_text(master)
        print_button(master)
        



#Checkbutton(master, text="操作", variable=var, command=callback).pack()

master['menu']=menubar
master.title("create bt scripe")
display = App(master)
master.mainloop()