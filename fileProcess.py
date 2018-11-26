# -*- coding: UTF-8 -*-
# fileName: output_len_ver.py
# Description: For 200U packaging
# Version: 1.01
# Time: 2018-8-2 14:39
# Python: Python2.7.12
# PyModule: os, json, tkinter, askopenfilename
import os
from tkinter import *
from tkinter.filedialog import askdirectory
import re


# Select folder path
def selectPath():
    path = askdirectory()
    return path

# Find files under the folder
def findFile(path, node):
	size=len(path)
	node.textMessage.delete('1.0','end')
	for fpathe,dirs,fs in os.walk(path):
		for f in fs:
			# 在消息框输出指定文件夹下的所有文件
			node.textMessage.insert(INSERT, os.path.join(fpathe,f)[int(size)+1:])
			node.textMessage.insert(INSERT,'\n') 
			print os.path.join(fpathe,f)[int(size)+1:]


# Get item info
def getItemInfo(path, node):
	file_name=path.split("/")[-1]
	print file_name
	file_info=file_name.split("_")
	for index in range(len(file_info)):
		if 0 == file_info[index].find("NW"): #搜索包含的特定字符窜
			print file_info[index]
			node.textItem.insert(INSERT,file_info[index])
		if 1 == index:
			node.textCompany.insert(INSERT, file_info[index])
		if 2 == index:
			node.textProject.insert(INSERT, file_info[index])
		if 3 == index:
			node.textVersion.insert(INSERT, file_info[index])
		if 4 == index:
			node.textTime.insert(INSERT,file_info[index])

#def getFirmwareInfo(node)
