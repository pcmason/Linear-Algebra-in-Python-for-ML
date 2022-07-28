#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 22:44:25 2022

@author: paulmason
"""

#Examples of methods to create different types of matrices using numpy

import numpy as np

#Create and output a basic 3X3 matrix
mat = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
print('\nBasic Matrix:')
print(mat)

#Create and output lower and upper triangular matrices from mat
lower = np.tril(mat)
print('\nLower Triangular Matrix:')
print(lower)
upper = np.triu(mat)
print('\nUpper Triangular Matrix:')
print(upper)

#Create and output diagonal vector from mat
dVec = np.diag(mat)
print('\nDiagonal Vector:')
print(dVec)

#Convert dVec into a diagonal matrix
dMat = np.diag(dVec)
print('\nDiagonal Matrix:')
print(dMat)

#Create and output a size 3 identity matrix
I = np.identity(3)
print('\nIdentity Matrix I3:')
print(I)

#Create and output a 2X2 othorgonal matrix
Q = np.array([[1, 0], [0, -1]])
print('\nOrthogonal Matrix:')
print(Q)

#Check if the Q^T equals the inverse of Q
inv = np.linalg.inv(Q)
print('\nQ^T:')
print(Q.T)
print('\nQ^-1:')
print(inv)

#Check if the dot product of Q and Q^T = I
idCheck = Q.dot(Q.T)
print('\nIdentity Equivalence:')
print(idCheck)