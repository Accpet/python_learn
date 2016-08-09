# -*- coding: UTF-8 -*-
__author__ = 'water'
import os
#!/usr/bin/python
f=open("shop1.txt",'r+')
# str=f.read(10);
# print "你读的字符串是：" ,str
#
# #查找当前位置
# position=f.tell();
# print position
# print os.getcwd()

a=f.readlines()
for i in a:
    print i