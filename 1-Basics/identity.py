#Identity matrix : square matrix with 1's on diagonal and zeros else where,  eye(shape)
import numpy as np 
id_array4 = np.eye(4) # 4 x 4 identity
print(id_array4)
id_array3 = np.eye(3)
print(id_array3)
id_array1 = np.eye(1)
print(id_array1)
id_array1 = np.eye(2)
print(id_array1)
'''4D'''
# [[1. 0. 0. 0.] 
#  [0. 1. 0. 0.] 
#  [0. 0. 1. 0.] 
#  [0. 0. 0. 1.]]
'''3D'''
# [[1. 0. 0.] 
#  [0. 1. 0.] 
#  [0. 0. 1.]]
'''1D'''
# [[1.]]   
'''2D'''
#[[1. 0.]    
#[0. 1.]]      