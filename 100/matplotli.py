#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'water'
'''
Created on Jul 12, 2014
python 科学计算学习：numpy快速处理数据测试
@author: 皮皮
'''
import string
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    file = open("shop1.txt", 'r')
    linesList = file.readlines()
#     print(linesList)
    linesList = [line.strip().split() for line in linesList]
    file.close()
    print linesList[:]
    print (linesList)
#     years = [string.atof(x[0]) for x in linesList]
    years = [x[0] for x in linesList]
    print(years)
    price = [x[1] for x in linesList]
    print(price)
    plt.plot(years, price, 'b*')#,label=$cos(x^2)$)
    plt.plot(years, price, 'r')
    plt.xlabel(years+2000)
    plt.ylabel(price*2000)
    plt.ylim(0, 15)
    plt.title('line_regression & gradient decrease')
    plt.legend()
    plt.show()
