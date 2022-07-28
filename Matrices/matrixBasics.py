#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 16:06:04 2022

@author: paulmason
"""
#Worked example working as an introduction to working with matrices in Python, specifically with numpy

import numpy as np

#Create and output a matrix
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)

#Add 2 matrices together
b =  a
c = a + b
print(c)

#Subtract 2 matrices 
d = a - b
print(d)

#Element wise matrix multiplication
e = a * b
print(e)

#Divide one matrix by another
f = a / b
print(f)

#Create 2 new arrays to use dot product on
g = np.array([[1, 2], [3, 4], [5, 6]])
h = np.array([[1, 2], [3, 4]])
i = g.dot(h)
print(i)

#Create a vector then multiply g by the vector showing matrix-vector multiplication
v = np.array([0.5, 0.5])
j = g @ v
print(j)

#Now multiply g by the scalar 0.5 to show matrix-scalar multiplication
num = 0.5
k = g * num
print(k)
