#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 00:39:07 2022

@author: paulmason
"""
#Worked example of indexing, slicing and reshaping numpy arrays

#Import numpy
import numpy as np

#Convert 1D list to an array
#Create a list of data
l = [11, 22, 33, 44, 55]

#Convert to a numpy array of data and output
data = np.array(l)
print(data)
print(type(data))

#Get first and last element of data using indexing
print(data[0])
print(data[4])

#Same as above, except last then first, using negative indexing
print(data[-1])
print(data[-5])

#Example of 1D slicing
#Output data
print(data[:])
#Get the first item in data using slicing
print(data[0:1])
#Use negative indexing and retrieve the last 2 items in data
print(data[-2:])

#Output shape of data
print(data.shape)

#Reshape 1D data to be a 2D array
data = data.reshape((data.shape[0], 1))
print(data.shape)

#Convert 2D list to an array
l = [[11, 22, 33],
     [44, 55, 66],
     [77, 88, 99]]

#Convert to numpy array and output
data = np.array(l)
print(data)
print(type(data))

#Get first item in 2D data
print(data[0, 0])
#Get all data from the first row
print(data[0, ])

#Split 2D dataset like loaded data would be in a ML project (output var is last column, rest of data is input vars)
x = data[:, :-1]
y = data[:, -1]
#Output data
print(x)
print(y)

#Split dataset into test and train dataset using a contrived split value of 2
split = 2
train = data[:split, :]
test = data[split:, :]
print(train)
print(test)

#Output shape of data and output number of rows and columns
print(data.shape)
print("Number of Rows: %d" % data.shape[0])
print('Number of Columns: %d' % data.shape[1])

#Reshape 2D data to a 3D array
data = data.reshape((data.shape[0], data.shape[1], 1))
print(data.shape)

