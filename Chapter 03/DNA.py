#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 12:39:56 2017

@author: janusboandersen
"""
import random

#Create a random DNA sequence
def generate_dna(N = 100):
    alphabet = list('ATCG')
    dna = [random.choice(alphabet) for i in range(N)]
    dna = ''.join(dna)
    return dna
#end func

#try it out
dna = generate_dna(600000)
