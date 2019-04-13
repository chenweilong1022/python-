#!/usr/bin/python
# -*- coding: UTF-8 -*-
# python文件io

# var = input("请输入文字:")
# print("您输入的是:",var)


file = open("C:\\Users\\Administrator\\Desktop\\yinzhi.txt",'r+')

# print(file.name)
# print(file.closed)
# print(file.mode)
# file.close()
# print(file.name)
# file.write("www.baidu.com")
# file.close()
# var = file.read(20)
# # print(var)
#
# print(var)
# print()
#
# print(file.tell(),"当前文件位置")
# file.seek(0,0)
# var1 = file.read(20)
# print(var1)

import os

# os.rename("main.py","main.py.bak")

# os.remove("main.py.bak")

# os.mkdir("newdir")
# os.chdir("newdir")
#
# file = open("test.txt","w")
# file.write("woshishuaibi")
# file.close()

print(os.getcwd())