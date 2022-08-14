#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 23:24:02 2022

@author: paulmason
"""
#Code that manually and reusably calculates the Principal Component Analysis (PCA)

import numpy as np

#Define a matrix
mat = np.array([[1, 2], [3, 4], [5, 6]])
print('Matrix:')
print(mat)

#Calculate the mean of each column
M = np.mean(mat.T, axis = 1)
print('\nColumn Means:')
print(M)

#Center columns by subtracting column means
C = mat - M
print('\nCentered Columns:')
print(C)

#Calculate covariance matrix of centered matrix
V = np.cov(C.T)
print('\nCovariance Matrix:')
print(V)

#Eigendecomposition of covariance matrix
values, vectors = np.linalg.eig(V)
print('\nEigenvalues:')
print(values)
print('\nEigenvectors:')
print(vectors)

#Proeject data
P = vectors.T.dot(C.T)
print('\nProjected Data:')
print(P.T)

#Calculate PCA using sklearn on mat
import sklearn.decomposition as skd

#Create PCA instance on mat with number of components set to 2
pca = skd.PCA(2)

#Fit on data
pca.fit(mat)

#Access Eigenvalues and vectors
print('\nPCA Eigenvalues:')
print(pca.components_)
print('\nPCA Eigenvectors:')
print(pca.explained_variance_)

#Transform the data
B = pca.transform(mat)
print('\nTransformed data:')
print(B)
