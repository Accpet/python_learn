#__author__ = 'water'
#-*- coding: UTF-8 -*-
# try:
#     print 'try...'
#     r=10 / 0
#     print 'result:',r
# except ZeroDivisionError,r:
#     print 'except:',r
# finally:
#     pass
# print 'finally'\
r=1
try:
    print 'try...'
    r=10 / 0
    print 'result:',r
except:
    print 'except:',r
finally:
    pass
print 'finally'
