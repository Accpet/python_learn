#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'water'
import Image
image = Image.open("1.jpg")
image.thumbnail((32,32))
image.show()