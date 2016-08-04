__author__ = 'water'
from ctypes import *
user32 = windll.LoadLibrary('user32.dll')
user32.LockWorkStation()

