#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 22:14:45 2017

@author: janusboandersen
"""

#2nd order differential

def diff2nd(f, x, h=1E-4):
    """
    diff2nd(f, x) numerically computes the second-order differential of a 
    function f around the point x.
    The optional argument h determines the differentiation band around x+/-h.
    """
    
    r = (f(x-h) - 2*f(x) + f(x+h))/float(h*h)
    return r
#end func

#Try it out
def g(t):
    return t**(-6)
#end func

t = 1.
d2g = diff2nd(g, t)

print(d2g)

import sympy as sp
t_symb = sp.symbols('t_symb')
g_symb = sp.Function('g_symb')
g_symb = t_symb**(-6)
d2g_symb = sp.diff(g_symb,t_symb,2)
g2 = sp.lambdify(t_symb, d2g_symb)
print(d2g_symb)
print(g2(t))

    