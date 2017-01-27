# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Cook the perfect egg

from math import pi, log as ln

#Variables
M = 67              # Mass in [grams] - small egg is 47 grams, large egg is 67 grams
rho = 1.038         # Density in [g cm^-3]
c = 3.7             # Specific heat capacity in [J g^-1 K^-1]
K = 5.4 * 10**-3    # Conductivity in [W cm^-1 K^-1]
Tw = 100            # Temperature of water (boiling) in [degrees Celsius]
To = 20             # Temperature (original) of egg when removed from fridge =0 or room temperature =20 in [degrees Celsius]
Ty = 70             # Temperature of coagulation for the egg yolk in [degrees Celsius]

#Compute time in [s] for the center of the yolk to reach the temperature Ty

t = ((M**(2/3.)*c*rho**(1/3.))/(K*pi*pi*(4*pi/3.)**(2/3)))*ln(0.76*((To-Tw)/(Ty-Tw)))

print("Boil the egg for %.2f minutes" % (t/60))
