#concatinate adding arrays
import numpy as np
array1 = np.array([0,1,2])
array2 = np.array([3,4,5])
print(np.concatenate((array1,array2))) #[0 1 2 3 4 5]
print(np.concatenate((array1,array2),axis=0)) #0 means row and is default
