# -*- coding: utf-8 -*-
__author__ = 'water'

import commands
import os
#os.system('dir')
#
# ### echo $? 0代表成功执行 echo $?非0代表失败
# cur_dir = os.system('dir')
# print cur_dir
#
# cur_dir=os.popen('pwd').read()
# print cur_dir

res=commands.getstatusoutput('dir')
print res
print 'hello,world'
print "怀朔"
os.walk('.')
11111
