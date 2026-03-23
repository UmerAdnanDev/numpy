# Reshaping changing an arrays dimensions without changing it's values
import numpy as n 
ar1 = n.array([1,2,3,4,5,6])

print(ar1.reshape(3,2))
print(ar1.reshape(6,1))