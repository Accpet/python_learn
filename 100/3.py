#__author__ = 'water'
# -*- coding: UTF-8 -*-
#/usr/bin/python
try:
    print 'this is try test..'
    f=open("shop4.txt",'w')
    f.write("你好 世界")
except IOError:
    print 'Error:no found file or dirtory file'
except :
    pass
else:
    print "hello,world..."
    print 'susssfully ...'
    f.close()
