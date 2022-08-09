#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 22:35:13 2022

@author: paulmason
"""
#Worked example of matrix factorization techniques

import numpy as np
import scipy.linalg as sp

#Define a square 3X3 matrix
mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('Matrix:')
print(mat)

#Calculate the lu decomposition of mat
P, L, U = sp.lu(mat)
print('\nP:')
print(P)
print('\nL:')
print(L)
print('\nU:')
print(U)

#Reconstruct the original mat using the dot product of P, L and U
mat_recon = P.dot(L).dot(U)
print('\nReconstructed Matrix:')
print(mat_recon)

#Make a rectangular 3X2 matrix
rect_mat = np.array([[1, 2], [3, 4], [5, 6]])
print('\nRectangular Matrix:')
print(rect_mat)

#Perform QR decomposition on rect_mat
Q, R = np.linalg.qr(rect_mat, 'complete')
print('\nQ:')
print(Q)
print('\nR:')
print(R)

#Reconstruct rect_mat
rect_mat_recon = Q.dot(R)
print('\nReconstructed Rectangular Matrix:')
print(rect_mat_recon)

#Create a 3X3 symmetric matrix
sym_mat = np.array([[2, 1, 1], [1, 2, 1], [1, 1, 2]])
print('\nSymmetric Matrix:')
print(sym_mat)

#Calculate cholesky decomposition on sym_mat
L = np.linalg.cholesky(sym_mat)
print('\nCholesky Decomposition L:')
print(L)

#Reconstruct sym_mat with L and its transposition
sym_mat_recon = L.dot(L.T)
print('\nReconstructed Symmetric Matrix:')
print(sym_mat_recon)