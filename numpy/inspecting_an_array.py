import numpy as np

# arr = np.array([[10,20,30,40] , [50,60,70,80] ,  [20,40,60,80]])
arr = np.array([[10,20,30,40] , [50,60,70,80]])
print(arr.shape) # this method tell the shape of the array
print(len(arr)) # this method is used to tell the number of elements in an array
print(np.ndim(arr)) # this method is used to tell the dimensionality of an array
print(np.size(arr)) # this method is used to tell the total number of elements in an array
print(type(arr)) # this method is used to tell the type of variable
print(arr.dtype) # this method is used to tell the data-type of a particular element in an array
print(arr.astype(float))
