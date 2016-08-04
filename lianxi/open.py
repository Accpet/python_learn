#-*- coding: UTF-8 -*-
__author__ = 'water'
try:
    f = open('f:/user_name', 'r')
    print f.read()
finally:
    if f:
      f.close()

with open('/path/to/file', 'r') as f:
    print f.read()

# try:
#     f = open('/path/to/file', 'r')
#     print f.read()
# finally:
#     if f:
#         f.close()