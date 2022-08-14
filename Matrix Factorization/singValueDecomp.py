#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 20:41:49 2022

@author: paulmason
"""
#Worked example of singular-value decomposition (SVD) in python. 

import numpy as np
import scipy.linalg as sp
import sklearn.decomposition as skl

#Define a matrix
mat = np.array([[1, 2], [3, 4], [5, 6]])
print('Original Matrix:')
print(mat)

#Run SVD on mat
U, s, VT = sp.svd(mat)
print('\nLeft Singular Vectors of mat:')
print(U)
print('\nSingular Values of mat:')
print(s)
print('\nRight Singular Vectors of mat:')
print(VT)

#Create m x n sigma matrix
Sigma = np.zeros((mat.shape[0], mat.shape[1]))
#Populate sigma with n x n diagonal matrix
Sigma[:mat.shape[1], :mat.shape[1]] = np.diag(s)
#Reconstruct original matrix
mat_recon = U.dot(Sigma.dot(VT))
print('\nReconstruction of Original Matrix:')
print(mat_recon)

#Define a new matrix to calculate the pseudoinverse on
mat2 = np.array([[0.1, 0.2], [0.3, 0.4], [0.5, 0.6], [0.7, 0.8]])
print('\nNew Matrix:')
print(mat2)

#Calculate pseudoinverse
ps = sp.pinv(mat2)
print('\nPsuedoinverse of New Matrix:')
print(ps)

#Calculate psuedoinverse manually using SVD
U, s, VT = sp.svd(mat2)
#Reciprocals of s
d = 1.0 / s
#Create m x n D matrix
D = np.zeros(mat2.shape)
#Populate D with n x n diagonal matrix
D[:mat2.shape[1], :mat2.shape[1]] = np.diag(d)
#Calculate psuedoinverse from svd 
svd_ps = VT.T.dot(D.T).dot(U.T)
print('\nPsuedoinvers of New Matrix Calculated using SVD:')
print(svd_ps)

#Example of dimensionality reduction using SVD
#Define a new matrix
mat3 = np.array([
	[1,2,3,4,5,6,7,8,9,10],
	[11,12,13,14,15,16,17,18,19,20],
	[21,22,23,24,25,26,27,28,29,30]])
print('\nMatrix for Dimensionality Reduction:')
print(mat3)

#Get SVD of mat3
U, s, VT = sp.svd(mat3)
#Create m x n sigma matrix
Sigma = np.zeros((mat3.shape[0], mat3.shape[1]))
#Populate Sigma with n x n diagonal matrix
Sigma[: mat3.shape[0], : mat3.shape[0]] = np.diag(s)
#Select only the first 2 features
n_elements = 2
Sigma = Sigma[:, :n_elements]
VT = VT[:n_elements, :]
#Reconstruct
mat3_recon = U.dot(Sigma.dot(VT))
print('\nReconstructed New Matrix:')
print(mat3_recon)
#transform
T = U.dot(Sigma)
print('\nFirst Transformation Calculation:')
print(T)
T = mat3.dot(VT.T)
print('\nSecond Transformation Calculation:')
print(T)

#Example on mat3 using TruncatedSVD()
svd = skl.TruncatedSVD(n_components = 2)
svd.fit(mat3)
result = svd.transform(mat3)
print('\nThird Transformation Calculation:')
print(result)