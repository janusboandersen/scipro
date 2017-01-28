#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 19:16:00 2017

@author: janusboandersen
"""
gv = 100

def test():
    global gv
    gv = 200

test()
print(gv)