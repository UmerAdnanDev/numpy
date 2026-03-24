#adds a new item to the end of an array
import numpy as n 
a1 = n.array([1,2,3])
print(n.append(a1,4)) # (array,item) -> [1 2 3 4]
a2 = n.array([[1,-1],[2,-2],[3,-3]])
print(n.append(a2,[4,-4])) #[ 1 -1  2 -2  3 -3  4 -4]