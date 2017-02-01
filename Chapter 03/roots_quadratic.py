#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 00:05:47 2017

@author: janusboandersen
"""
import numpy.lib.scimath as scm

#Compute the roots (real or complex) of 2nd degree polynomials
def roots(a=1, b=0, c=0):
    """
    Computes the real and/or complex roots of a 2nd degree polynomial,
    which shall be specified as ax^2 + bx + c = 0.
    """
    d = b**2 - 4*a*c  #discriminant
    
    if d > 0:  #2 real roots
        r1 = ((-b) + scm.sqrt(d))/float(2*a)
        r2 = ((-b) - scm.sqrt(d))/float(2*a)
        return r1, r2

    elif d == 0: # 1 real root
        r1 = -b / float(2*a)
        return r1, r1
    
    elif d < 0: # 2 complex roots
        r1 = ((-b) + scm.sqrt(d))/float(2*a)
        r2 = ((-b) - scm.sqrt(d))/float(2*a)
        return r1, r2
    #end if  
#end def

def test_roots_real():
    a = 1
    b = 0
    c = 0
    test = roots(a, b, c)
    exact = (0, 0)
    success = test == exact
    msg = "Test of {}x^2 + {}x + {} = 0 produced roots {} vs. expected result {}".format(a, b, c, test, exact)
    assert success, msg
#end def

def test_roots_complex():
    a = 1
    b = 0
    c = 1
    test = roots(a, b, c)
    exact = (1j, -1j)
    success = test == exact
    msg = "Test of {}x^2 + {}x + {} = 0 produced roots {} vs. expected result {}".format(a, b, c, test, exact)
    assert success, msg
#end def