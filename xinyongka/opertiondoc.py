__author__ = 'water'
import os
# print os.name
# #print os.uname
# print os.environ
# ##D:\python\xinyongka
# print os.path.abspath('.')
# print os.path.join('D:\python\\xinyongka','xinyongka')
# print os.mkdir('D:\python\try')

print [x for x in os.listdir('.') if os.path.splitext(x)[1]=='.py']