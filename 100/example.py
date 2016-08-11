#!/usr/bin/python
# -*- coding: UTF-8 -*-
#python tkinter image

from Tkinter import *
import ImageTk
import time
# table = Tk()
# table.title("hello world")
# table.geometry('1200x800')
# aa=Button(table,text='抽奖',width(100))
# aa.pack()

# Label(table, text="abc", image=img).pack(side="top")
# table.mainloop()
from Tkinter import *

def rc():
    global n
    file_name=''
    f=(n%2==1)
    while f:
        for i in range(1,6):                         #img.destroy()
            time.sleep(.1)
            file_name=str(i)+'.jpg'
            img = ImageTk.PhotoImage(file=file_name,width=100,height=100)
            Label(root, text="员工", image=img)
def  hello(event):
    global n
    n+=1
    if n %2==1:
     #  l = Label(root, text="hello", bg="green", font=("Arial", 12), width=5, height=2)
       print "抽奖开始...."
    # #  l.pack(side=LEFT)
       rc()
    else:
      # l = Label(root, text="wrold", bg="green", font=("Arial", 12), width=5, height=2)
       print "抽奖结束..."
       rc()
      # l.pack(side=LEFT)
      ## root.mainloop()

n=0
root = Tk()
root.title("抽奖软件")
root.iconwindow()
root.geometry('800x600')
root.resizable(width=False, height=True)
l = Label(root, text="show", bg="green", font=("Arial", 12), width=5, height=2)
b=Button(root,text='抽奖',width=40,height=2)
b.bind('<Button-1>',hello)
b.pack(side=BOTTOM)
#l.pack(side=TOP)  #这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
root.mainloop()
