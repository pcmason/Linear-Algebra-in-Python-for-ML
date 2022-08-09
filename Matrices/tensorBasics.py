#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 21:28:56 2022

@author: paulmason
"""
#Worked example using tensors

import numpy as np

#Create a tensor using the array() method from np
A = np.array([
  [[1,2,3],    [4,5,6],    [7,8,9]],
  [[11,12,13], [14,15,16], [17,18,19]],
  [[21,22,23], [24,25,26], [27,28,29]],
  ])

print('Shape of the tensor:')
print(A.shape)
print('\nTensor:')
print(A)

#Create a new tensor B, equal to A, and add the 2 together
B = A
C = A + B
print('\nOutput of tensor addition:')
print(C)

#Subtract tensor B from A
D = A - B
print('\nOutput of tensor subtraction:')
print(D)

#Get Hadamard Product of A and B
E = A * B
print('\nOutput of tensor Hadamard Product:')
print(E)

#Divide tensor A by B
F = A / B
print('\nOutput of tensor division:')
print(F)

#Calculate the tensor product of A and B (Uncomment for a wild tensor output)
#G = np.tensordot(A, B, axes = 0)
#print('\nOutput of tensor product:')
#print(G)

#Chiller tensor product to calculate
H = np.array([1, 2])
I = np.array([3, 4])
G = np.tensordot(H, I, axes = 0)
print('\nOutput of tensor product:')
print(G)