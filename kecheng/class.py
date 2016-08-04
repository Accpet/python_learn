#_*_ coding: UTF-8 _*_
__author__ = 'water'

#相对一个用户模块
class myclass:
    def __init__(self):
        print 'hello,world ...'
        self.name='Huai Shuo'
    def setname(self,name):
        self.name=name
    def printname(self):
        print self.name

class mynewclass(myclass):
    def setage(self,age):
        self.age=age
    def printage(self):
        print self.age


# a=myclass()
# a.setname("Apple")
# # a.printname()
# print a.name
a=mynewclass()

a.setname('huai shuo')
a.setage('27')
a.printname()
a.printage()