# -*- coding: UTF-8 -*-
# fileName: mainWindow.py
# Description: For 200U packaging
# Version: 1.01
# Time: 2018-11-23 11:32
# Python: Python2.7.12
# PyModule: tkFont, tkinter, messagebox, command

from Tkinter import *
from distutils import command
from tkinter import messagebox
import tkinter.font as tkFont


# Personal module
import fileProcess as fP


master = Tk()
master.geometry("580x400+300+100")#窗口大小，位置



def print_button(master):
    btnSelect = Button(master, text="Select", width=7, height=1, command=file_callback)
    btnSelect.place(x=500, y=10, anchor = 'nw')

    btnSelect = Button(master, text="Find", width=7, height=1, command=file_callback)
    btnSelect.place(x=500, y=50, anchor = 'nw')

    btnSelect = Button(master, text="Update", width=7, height=1, command=file_callback)
    btnSelect.place(x=500, y=90, anchor = 'nw')


class textNode:
    def __init_(self):
        self.textFile
        self.textOTA
        self.textInfact
        self.textFact
        self.textItem
        self.textVersion
        self.textTime
        self.textCompany
        self.textProject
        self.textMessage

Node = textNode() #定义文本框管理类


def print_text(master, Node):
    #打印文本框
    testFont = tkFont.Font(family='Fixdsys', size=12)

    Node.textFile = Text(master, width=50, height=1, font=testFont)
    Node.textFile.place(x=80, y=10, anchor='nw')
    #Node.textFile.insert(INSERT,'Please select file')

    Node.textOTA = Text(master, width=50, height=1, font=testFont)
    Node.textOTA.place(x=80, y=50, anchor='nw')

    Node.textInfact = Text(master, width=50, height=1, font=testFont)
    Node.textInfact.place(x=80, y=90, anchor='nw')

    Node.textFact = Text(master, width=50, height=1, font=testFont)
    Node.textFact.place(x=80, y=130, anchor='nw')

    Node.textItem = Text(master, width=8, height=1, font=testFont)
    Node.textItem.place(x=80, y=200, anchor='nw')

    Node.textVersion = Text(master, width=15, height=1, font=testFont)
    Node.textVersion.place(x=230, y=200, anchor='nw')

    Node.textTime = Text(master, width=15, height=1, font=testFont)
    Node.textTime.place(x=420, y=200, anchor='nw')

    Node.textCompany = Text(master, width=15, height=1, font=testFont)
    Node.textCompany.place(x=80, y=240, anchor='nw')

    Node.textProject = Text(master, width=20, height=1, font=testFont)
    Node.textProject.place(x=280, y=240, anchor='nw')


    #Node.textMessage = Text(master, width=58, height=6, font=testFont)
    #Node.textMessage.place(x=80, y=280, anchor='nw')

 
    Node.textMessage = Text(master, width=58, height=6, font=testFont)
    # 创建滚动条
    scroll = Scrollbar(master,borderwidth=3)
    # 将滚动条与文本框关联
    Node.textMessage.config(yscrollcommand=scroll.set) # 将滚动条关联到文本框
    scroll['command']=Node.textMessage.yview
    scroll.place(x=550, y=280, anchor='nw')
    #scroll.grid(row=5,column=6) # side是滚动条放置的位置，上下左右。fill是将滚动条沿着y轴填充
    Node.textMessage.place(x=80, y=280, anchor='nw')
    
    

    Node.textMessage.insert(INSERT, 'hello world\n')
    Node.textMessage.insert(INSERT, '1234567')


def print_label(master):
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



#为顶级菜单实例添加菜单，并级联相应的子菜单实例    
menubar.add_cascade(label='文件', menu=fmenu)
menubar.add_cascade(label='操作', menu=vmenu)
menubar.add_cascade(label='设置', menu=smenu)
menubar.add_cascade(label='帮助', menu=hmenu)


def file_callback():
    print "file callback"
    Node.textFile.delete(0.0, END)
    Node.textFile.insert(INSERT,fP.selectPath())
   
    str_size =Node.textFile.get("0.0", "end").strip('\n')
    fP.findFile(str_size, Node)


    #messagebox.showinfo('复制', '编辑-复制！')  # 消息提示框

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
        print_label(master)
        print_text(master, Node)
        print_button(master)
        #Node.textTime.insert(INSERT,'Please select file')
        



#Checkbutton(master, text="操作", variable=var, command=callback).pack()

master['menu']=menubar
master.title("Python GUI")
display = App(master)
master.mainloop()