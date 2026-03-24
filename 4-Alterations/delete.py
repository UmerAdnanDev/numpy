#delete(array,index) to remove an item
import numpy as n
a1 = n.array([0,1,2,3])
print(n.delete(a1,0)) #[1 2 3]
a2 = n.array([[0,1],[2,3]])
print(n.delete(a2,0))#[1 2 3]
print(n.delete(a2,3))#[0 1 2]
print(n.delete(a2,1,axis=0)) #[[0 1]]
print(n.delete(a2,1,axis=1)) # removes index 1 item fronm each sun array 
# [[0]
#  [2]]