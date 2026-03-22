# used to get multiple items at different indexes
import numpy as np
array = np.array([1,2,3,4,5,6,7,8,9])
                # 0 1 2 3 4 5 6 7 8
               # -9-8-7-6-5-4-3-2-1  
print(array[[2,0,4,8]]) # -> [3 1 5 9] 
print(array[[-2,0,-4,1]])# -> [8 1 6 2]
