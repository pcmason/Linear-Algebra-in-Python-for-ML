#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 21:14:55 2022

@author: paulmason
"""
#Basic example code going over common uses of numpy for easy reference code

#Of course begin by importing numpy
import numpy as np

#Create a list and turn it into a numpy array
l = [1.0, 2.0, 3.0]
a = np.array(l)

#Output the array itself, its shape and data type
print(a)
print(a.shape)
print(a.dtype)

#Different examples of methods to create numpy arrays
#Create an empty array
emp = np.empty([3, 3])
print(emp)

#Create an array filled with 0s
z = np.zeros([3, 5])
print(z)

#Create an array filled with 1s
o = np.ones([6, 3])
print(o)

#Now show off 2 methods for combining arrays, first create 2 arrays of same size
a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])
print(a1)
print(a2)

#Stacking arrays vertically using VStack
a3 = np.vstack((a1, a2))
print(a3)
print(a3.shape)

#Stacking arrays horizontally using Hstack
a4 = np.hstack((a1, a2))
print(a4)
print(a4.shape)
