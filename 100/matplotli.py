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
##import numpy as np

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x**2)

plt.figure(figsize=(8,4))
plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2)
plt.plot(x,z,"b--",label="$cos(x^2)$")
plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("PyPlot First Example")
plt.ylim(-1.2,1.2)
plt.legend()
plt.show()