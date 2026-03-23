# flattening : changing the dimensions of an array (multi -> 1D)
'''ravel() & flatten()'''
import numpy as n
ar2d =n.array([[1,2],[3,4],[5,6]])
print(ar2d)
print(ar2d.ravel())
print(ar2d.flatten())