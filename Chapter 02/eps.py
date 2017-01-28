#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 18:26:14 2017

@author: janusboandersen
"""

#Errors
eps = 1.0
while 1.0 != 1.0 + eps:
    print("..........", eps)
    eps /= 2.0
print("Final eps:", eps)
