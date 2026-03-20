# dtype tells the data type of array
import numpy as np
array1 = np.array([9,0,3.7])
array2 = np.array([9,0,'3'])
array3 = np.array([9,0,True])
array4 = np.array(['0','1','2'])
print(array1.dtype) #float64
print(array2.dtype) #<U21 
print(array3.dtype) #int64
print(array4.dtype) #<U1