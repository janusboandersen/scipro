#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 13:32:29 2017

@author: janusboandersen
"""

#Convert from metric to imperial units
def convert(input):
    """
    input a length in meters [m] and get a text string of the
    equivalent length in various imperial units
    """

    #constants
    m2cm = 100.
    inch2cm = 2.54
    foot2inch = 12
    yard2foot = 3
    mile2yard = 1760

    #calculations
    inches = input * m2cm / inch2cm
    feet = inches / foot2inch
    yards = feet / yard2foot
    miles = yards / mile2yard
    
    
    output = """
    {input} meters equals:
    {inches: .2f} inches
    {feet: .2f} feet
    {yards: .2f} yards
    {miles: .2f} miles""".format(input=input, inches=inches, feet=feet, yards=yards, miles=miles)
    
    print(output)
    