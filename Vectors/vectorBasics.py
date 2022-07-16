#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 15:33:57 2022

@author: paulmason
"""

#Worked example of vector creation and arithmetic

#Import numpy
import numpy as np

#Create and output a vector
v = np.array([1, 2, 3])
print(v)

#Create another vector 
a = np.array([4, 5, 6])
#print(a)
#Add v and a together
b = a + v
print(b)

#Subtract a and v
c = a - v
print(c)

#Multiply c and b
d = c * b
print(d)

#Divide d with a
e = d / a
print(e)

#Calculate the dot product of d and e
f = e.dot(d)
print(f)

#Calculate the dot product of c and e
g = c @ e
print(g)

#Create a scalar and mutliply the vector e by it
scalar = 7
h = scalar * e
print(h)