import numpy as np
array1 = np.array([1,2,3,4,5])
array2 = np.array([1,2,3,4,5,6])
#gets addition of all elements in array
print(np.sum(array1))
#gets minimum value in array
print(np.min(array1))
#gets maximum value in array
print(np.max(array1))
#gets mean(average) value in array
print(np.mean(array1))
#gets median value in array
print(np.median(array1))#odd array : middle value 
print(np.median(array2))#even array: average of two middle numbers
#gets variance (average squared difference from mean)in array
print(np.var(array1))
'''
i.e array = [1 2 3 4 5] 
mean = 3 
difference from mean = [-2 -1 0 1 2] here (original - mean)
squared = [4 1 0 1 4] squared difference from mean
variance = 4+1+0+1+4 / 5 => 2
'''
#gets standard deviation(square root of variance) in array
print(np.std(array1)) # √ variance => √2 => 1.4142....