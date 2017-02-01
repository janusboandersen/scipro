#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 15:02:59 2017

@author: janusboandersen
"""

#test

#success = 1 == 2 #will result in false
#msg = "failed, 1 does not equal 2"
#assert success, msg

try:
    10/1  #divide by zero
except ZeroDivisionError:
    print("stop dividing by zero!")
finally:
    print("Silly user!!")