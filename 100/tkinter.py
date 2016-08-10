#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'water'
import Tkinter as tkinter
#import numpy as np
import glob,os
top=tkinter.Tk()

li     = ['C','python','php','html','SQL','java']
movie  = ['CSS','jQuery','Bootstrap']
listb  = tkinter.Listbox(top)
listb2 = tkinter.Listbox(top)
for item in li:
    listb.insert(0,item)
for item in movie:
    listb2.insert(0,item)
button =tkinter.Button(top)
button.pack()
Canvas =tkinter.Canvas(top)
coord = 10, 50, 240, 210
Canvas.create_arc(coord,start=0,extent=150,fill="YELLOW")
#Canvas.create_arc(coord,start=150,extent=200,fill="RED")
Canvas.create_arc(coord,start=320,extent=360,fill="BLUE")
Canvas.pack()
top.mainloop()