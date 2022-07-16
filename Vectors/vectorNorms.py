#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 15:55:51 2022

@author: paulmason
"""
#Worked example calculated different vector norms/magnitudes

#Import numpy
import numpy as np

#Create example vector
v = np.array([1, 2, 3])
print(v)

#Calculate the l1 norm of v
l1 = np.linalg.norm(v, 1)
print(l1)

#Calculate the l2 norm of v
l2 = np.linalg.norm(v)
print(l2)

#Calculate the max norm of v
maxNorm = np.linalg.norm(v, np.inf)
print(maxNorm)