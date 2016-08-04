__author__ = 'water'
import os
import sys

# p='192.168.1.'
for i in range(1,255,1):
    p='192.168.1.'
    p=p+str(i)
    a = os.system("ping %s"%(p))
    print a
    if a!=0:
        print ''' %s is  down'''%(p)



