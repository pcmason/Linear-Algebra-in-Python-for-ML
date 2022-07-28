#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 23:37:38 2022

@author: paulmason
"""

#Worked Example of matrix operations in numpy

import numpy as np

mat = np.array([[1, 2], [3, 4], [5, 6]])
print('\nMatrix:')
print(mat)

#transpose mat
matT = mat.T
print('\nTransposed Matrix:')
print(matT)

#Create a matrix to be inverted
mat = np.array([[1.0, 2.0], [3.0, 4.0]])
print('\nMatrix:')
print(mat)

#Invert mat
matInv = np.linalg.inv(mat)
print('\nInverted Matrix:')
print(matInv)

#Ensure you got the inverse by calculating the identity matrix
I = mat.dot(matInv)
print('\nIdentity Matrix:')
print(I)

#Create a 3X3 matrix
mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('\nMatrix:')
print(mat)

#Calculate and output trace of mat
matTrace = np.trace(mat)
print('\nTrace of Matrix:')
print(matTrace)

print('\nMatrix:')
print(mat)
#Calculate and output the determinant of mat
detMat = np.linalg.det(mat)
print('\nMatrix Determinant:')
print(detMat)

#Create vector of scalar values and calculate its ranks
v1 = np.array([1, 2, 3])
print('\nVector1:')
print(v1)
v1Rank = np.linalg.matrix_rank(v1)
print('\nVector1 Rank: %d' % v1Rank)

#Create vector of 0 values and calculate its rank
v2 = np.array([0, 0, 0, 0])
print('\nVector2:')
print(v2)
v2Rank = np.linalg.matrix_rank(v2)
print('\nVector2 Rank: %d' % v2Rank)

#2X2 matrix of rank 0
mat1 = np.array([[0, 0], [0, 0]])
print('\nMatrix1')
print(mat1)
mat1R = np.linalg.matrix_rank(mat1)
print('\nMatrix1 Rank: %d' % mat1R)

#2X2 matrix of rank 1
mat2 = np.array([[1, 2], [1, 2]])
print('\nMatrix2:')
print(mat2)
mat2R = np.linalg.matrix_rank(mat2)
print('\nMatrix2 Rank: %d' % mat2R)

#2X2 matrix of rank 2
mat3 = np.array([[1, 2], [3, 4]])
print('\nMatrix3:')
print(mat3)
mat3R = np.linalg.matrix_rank(mat3)
print('\nMatrix3 Rank: %d' % mat3R)