#!/usr/bin/python
# -*- coding: UTF-8 -*-
#python tkinter image

from Tkinter import *
import ImageTk
# table = Tk()
# table.title("hello world")
# table.geometry('1200x800')
# aa=Button(table,text='抽奖',width(100))
# aa.pack()
# #table.resizable(width=False, height=True)
# img = ImageTk.PhotoImage(file='1.jpg')
# Label(table, text="abc", image=img).pack(side="top")
# table.mainloop()
from Tkinter import *
def  hello(event):
    global n
    n+=1
    if n %2==1:
       l = Label(root, text="hello", bg="green", font=("Arial", 12), width=5, height=2)
       print "抽奖开始...."
       l.pack(side=LEFT)
      # root.mainloop()
    else:
       l = Label(root, text="wrold", bg="green", font=("Arial", 12), width=5, height=2)
       print "抽奖结束..."
       l.pack(side=LEFT)
      # root.mainloop()
n=0
root = Tk()
root.title("抽奖软件")
root.iconwindow()
root.geometry('300x200')
l = Label(root, text="show", bg="green", font=("Arial", 12), width=5, height=2)
b=Button(root,text='抽奖',width=10,height=4)
b.bind('<Button-1>',hello)
b.pack(side=RIGHT)
l.pack(side=LEFT)  #这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
root.mainloop()
