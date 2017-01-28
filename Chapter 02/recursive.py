#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 19:27:18 2017

@author: janusboandersen
"""

#recursive approach to a sum
def L(x, n, i=1):
    if i == n:
        return (1./i)*(x/(1.+x))**i
    else:
        return (1./i)*(x/(1.+x))**i + L(x=x, n=n, i=i+1)
    #endif
#end func

def L2(x, n):
    s = 0
    for i in range(1, n+1):
        s += (1.0/i)*(x/(1.0+x))**i
    return s

print(L(x=5,n=10))
print(L2(x=5,n=10))

