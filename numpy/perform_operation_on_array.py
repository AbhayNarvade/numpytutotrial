# creation , indexing and slicing numpy arrays


import numpy as np

# arr = np.array([[10,20,30,40] , [50,60,70,80] ,  [20,40,60,80]])
arr = np.array([[10,20,30,40] , [50,60,70,80]])
# arr = np.array([10,20,30,40])
# print(arr)
# print(arr[:4]) # this is slicing for single dimension array
# print(arr[0:2, 0:3]) # this is slicing for multi dimension array
print(arr[1,2:4]) # this is slicing for multi dimension array
print(np.shape(arr))
print(np.size(arr))
print(np.ndim(arr))
print(arr.dtype)

print(type(arr))