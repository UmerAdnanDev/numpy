import numpy as np
float_array = np.array([1.1,2.0,4.9])
print(float_array)
print(float_array.dtype)
# [1.1 2.  4.9]
# float64
print()
int_array = float_array.astype(int)
print(int_array)
print(int_array.dtype)
# [1 2 4]
# int64
print()
str_array = float_array.astype(str)
print(str_array)
print(str_array.dtype)
# ['1.1' '2.0' '4.9']
# <U32