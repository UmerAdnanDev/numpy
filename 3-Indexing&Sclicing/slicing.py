# slicing [start : stop : step] i.e start is included and stop is excluded
array = [1,2,3,4,5]
print(array[:3]) # 0 : 3 : 1 -> [ 1 2 3 ]
print(array[2:]) # 2 : end : 1 -> [ 3 4 5 ]
print(array[::2]) # 0 or start : end : 2 -> [ 1 3 5]
print(array[: : -1]) # 0 : end : -1 -> [ 5 4 3 2 1 ]
print(array[1:3]) # 1 : 3 : 1 -> [ 2 3 ]

