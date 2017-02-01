#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 17:17:58 2017

@author: janusboandersen
"""

#numerical integration with Simpson's rule


def Simpson(f, a, b, n=500):
    """
    Simpson(f, a, b, n=500) -> Numerical integration of a function f over an
    interval [a;b], using n intervals (n=500 by default) for the approximation.
    The parameter n must be an even integer.
    
    Langtangen 4th ed. p. 124
    """
    
    #Test the supplied n:
    assert n%2 == 0, "Parameter n (intervals) must be an even integer."
    
    #Test the supplied integration limits
    assert b > a, "Integration limit b must be greater than a."
    
    #Calculate h, ensure floating point number
    h = (b-a)/float(n)
    
    #calculate the partial sums (this could likely be sped up by one loop)
    sf_0 = f(a)
    sf_1 = f(b)
    sf_2 = 0
    sf_3 = 0
    
    #Compute sf_2
    for i in range(1,n//2 + 1):
        sf_2 += f(a + (2*i - 1)*h)
    #end for    

    #Compute sf_3
    for i in range(1,n//2):
        sf_3 += f(a + 2*i*h)

    #Compute and return the Simpson's rule approximation
    s = (1/3.)*h*(sf_0 + sf_1 + 4*sf_2 + 2*sf_3)
    
    return s
#end def



#Test function
def test_simpson():
    """Check that the Simpson Rule is implemented correctly using a sinus and
    a polynomial function."""
    
    import math
    
    #test 1: with Sinus function
    h = lambda x: (3/2.)*math.sin(x)**3

    #Integration limits
    a = 0
    b = math.pi
    
    #Known result
    exact = 2
    
    #Run Simpson rule for h(x) over interval a to b
    test_case = Simpson(h, a, b)
    success = tol(test_case, exact)
    assert success, "test of integral of sin^3(x) over 0 to pi."
    
                             
                                              
    #test 2: with exact result using 2nd degree polynomial
    g = lambda x: 3*(x**2) - 7*x + 2.5      #2nd degree polynomial
    G = lambda x: x**3 - 3.5*(x**2) + 2.5*x   #Antiderivative of g(x)
    

    #Integration limits
    a = 1.5
    b = 2.0
    
    #Known result
    exact = G(b) - G(a)

    #Run Simpson rule for g(x) over interval a to b    
    test_case = Simpson(g, a, b)
    success = tol(test_case, exact)
    assert success, "test of integral of 3x^2 - 7x + 2.5 over 1.5 to 2."

#end def


def tol(a, b, tolerance=1E-5):
    return True if abs(a-b) < tolerance else False
#end def