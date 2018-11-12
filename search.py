#!/usr/nbin/python
# --*-- coding:utf-8 --*--
import re
import os

class FieldSearch:
	'字段查找基类'
	fpath = "./"

	'读取文件路径'
	def getDirPath:
		fpath = os.getcwd()

	#scan_files("/export/home/test/", prefix=".txt")
	def scanFiles(directory,prefix=None,postfix=None):
    	files_list=[]
	    for root, sub_dirs, files in os.walk(directory):
	        for special_file in files:
	            if postfix:
	                if special_file.endswith(postfix):
	                    files_list.append(os.path.join(root,special_file))
	            elif prefix:
	                if special_file.startswith(prefix):
	                    files_list.append(os.path.join(root,special_file))
	            else:
	                files_list.append(os.path.join(root,special_file))
                          
   		return files_list


	def  printFileField(filepath):
		logyzm = open("./Serial-COM4/hello.log").read()
		#print logyzm
		temp = logyzm.decode("utf8")
		findword = u"(.+no valid script file.+)"# .+表示匹配至少一个任意字符
		#findword = u"(.+您的验证码是.+)"#表示取有“您的验证码是”字符串的这行所有数据
		pattern = re.compile(findword)
		results = pattern.findall(temp)
		for result in results:
			print result