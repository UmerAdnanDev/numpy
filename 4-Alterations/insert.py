#insert(array,index,item,axis) axis can be skipped by default axis = 0 -> row
import numpy as n
# in 1D array
a1 = n.array([1,2,3,4,5,6,7])
print(n.insert(a1,0,0)) # [0 1 2 3 4 5 6 7]
print(n.insert(a1,7,-1))#[ 1  2  3  4  5  6  7 -1]
print(n.insert(a1,4,0.96))#[1 2 3 4 0 5 6 7]
# in 2D array
a2 = n.array([[1,2],[3,4],[5,6]])
print(n.insert(a2,0,[-1,0])) #[-1  0  1  2  3  4  5  6]
print(n.insert(a2,0,[-1,0],axis=0))
print(n.insert(a2,-1,[7,8],axis=0))
print(n.insert(a2,0,[-1,0],axis=None)) # None flattens the array
print(n.insert(a2,0,6,axis=1)) # all 1st columns got 6 
print(n.insert(a2,2,0,axis=1))
print(n.insert(a2,0,1,axis=0)) #??