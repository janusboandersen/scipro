#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 18:19:29 2016

@author: janusboandersen
"""

v0 = 5
g = 9.81
t = 0.6
y = v0*t - 0.5*g*(t)**2
print("At t=%g s, the height of the ball is %.2f m." %(t,y))
print("At t={t:g} s, the height of the ball is {y:.2f} m.".format(t=t,y=y))

