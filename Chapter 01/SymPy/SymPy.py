#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 16:58:41 2017

@author: janusboandersen
"""

#Symbolic manipulation with SymPy

from sympy import (symbols, diff, integrate, Rational, lambdify, solve)
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


t, v0, g = symbols('t v0 g')  #Define the symbols to use

y = v0*t - Rational(1,2)*g*t**2  #Define a symbolic equation/expression

#Differentiation of position, which yields the velocity, v
dydt = diff(y,t)  #Differentiate the equation w.r.t. t

#Differentiation of velocity, which yields the acceleration
d2y_dt2 = diff(y,t,t)  #2nd derivative of y: d/dt of d/dt of y
print("Acceleration:", d2y_dt2)

#Integration to recover vertical position from velocity
y2 = integrate(dydt,t)
print(y2)

#Turn symbolic expression into (anonymous) function for numeric evaluation
v = lambdify([t, v0, g], dydt)  #variables and the function

v_t = v(0, 5, 9.81)  #velocity at t=0, with v0=5, g=9.81
print("velocity at t=0, with v0=5, g=9.81:", v_t)

v_t = v(2, 5, 9.81)  #velocity at t=2, with v0=5, g=9.81
print("velocity at t=2, with v0=5, g=9.81:", v_t)


#build plot data for one experiment
v_0 = 50  #m/s
g_exp = 9.81  #m/s/s
t_0 = 0
t_end = 10

y_t = lambdify([t, v0, g], y)

t_label = "time, t"
y_label = "vert. pos., y"
v_label = "velocity, v"

data = pd.DataFrame(columns=(t_label, y_label, v_label))

index_time = enumerate(list(np.linspace(t_0, t_end, (t_end - t_0)*5 + 1)), 1)

for i, tt in index_time:
    data.loc[i] = tt, y_t(tt, v_0, g_exp), 0  #, v(tt, v_0, g_exp)
#end for

data.plot.line(x=t_label, y=y_label)

#solve for roots (y=0 and dy/dt=0)
roots = solve(y, t)
maxima = solve(dydt, t)

#What's the highest point? Symbolically.
parabola_max = y.subs(t, maxima[0])

#For a given set of values, find the highest point numerically:
hp = parabola_max.subs({v0: v_0, g: g_exp})
pl = """
Highest point: {max: .2f} [m] occurs at time {maxima}""".format(max=hp, maxima=maxima[0])
print(pl)



    