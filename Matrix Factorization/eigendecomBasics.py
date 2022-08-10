#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 22:12:55 2022

@author: paulmason
"""
#Worked example of a eigendecomposition on a square matrix

import numpy as np

#Create 3x3 square matrix
mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('Original 3x3 Square Matrix:')
print(mat)

#Calculate and output eigendecomposition of mat
values, vectors = np.linalg.eig(mat)
print('\nEigenvalues:')
print(values)
print('\nEigenvectors:')
print(vectors)

#Confirm the first eigenvector
#Reconstruct the first eigenvector mathematically
mat_recon = mat.dot(vectors[:, 0])
print('\nReconstructed First Eigenvector:')
print(mat_recon)
#Now just get the first eigenvector from what was calculated above
first_eig = vectors[:, 0] * values[0]
print('\nActual First Eigenvector:')
print(first_eig)

#Reconstruct original square matrix
#Create matrix from eigenvectors
Q = vectors
#Get inverse of Q
R = np.linalg.inv(Q)
#Create a diagonal matrix from the eigenvalues
L = np.diag(values)
#Reconstruc the original square matrix
mat_recon2 = Q.dot(L).dot(R)
print('\nReconstruction of the Original Square Matrix:')
print(mat_recon2)

