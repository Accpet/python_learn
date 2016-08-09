#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'water'

def temp_conver(var):
    try:
        return int(var)
    except ValueError, Argument:
        print "parameter no number\n",Argument

print temp_conver("dfdf")