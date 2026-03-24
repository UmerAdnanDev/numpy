#boolean masking filtering data on the basis of conditions
import numpy as np
a = np.array([1,2,3,4,5,6,7])
print(a[a%2==0]) # gives even items
print(a[a>=4])