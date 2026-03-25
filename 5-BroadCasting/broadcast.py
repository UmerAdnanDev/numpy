# The ability of numpy to allow arithmetic operations between arrays of different dimensions is know as broadcasting
#1 - by expanding the smaller array , 2 - doesn't work id dimensions are incompatible 
import numpy as n
a1 = n.array([1,2,3])
print(a1**4) # array and scalar operation [1 16 81]
a2 = n.array([[1],[2],[3]]) #2D array
print(a1+a2) # order doesn't matter the smaller array is expanded
print(a2+a1)
a3 = n.array([1,2])
print(a3+a2)
a4 = n.array([[1,2],[3,4],[5,6]])
print(a2*a4)
