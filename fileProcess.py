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


# Select folder path
def selectPath():
    path = askdirectory()
    return path

# Find files under the folder
def findFile(path, node):
	for fpathe,dirs,fs in os.walk(path):
		for f in fs:
			node.textMessage.insert(INSERT, os.path.join(fpathe,f))
			node.textMessage.insert(INSERT,'\n')
			node.textMessage.see(END)
			print os.path.join(fpathe,f)


