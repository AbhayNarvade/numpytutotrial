import numpy as np

# a = np.array([1,2,3])
# b = np.array([4,5,6])

# print(np.concatenate([a, b]))
# print(np.concatenate((a, b)))




# a = np.array([[1,2,3],[7,8,9]])
# b = np.array([[4,5,6] , [14,15,16]])

# print(np.concatenate((a, b) , axis = 1))


# a = np.array([[1,2,3],[7,8,9]])
# b = np.array([[4,5,6] , [14,15,16]])

# print(np.hstack((a, b) ))  # horizontal concatenation

# a = np.array([[1,2,3],[7,8,9]])
# b = np.array([[4,5,6] , [14,15,16]])

# print(np.vstack((a, b) ))  # vartical concatenation

# a = np.array([20,40,30,40,10,20])
# b = np.array_split(a , 3)
# print(b)


a = np.array([[1,2,3],[4,5,6,]])
b = np.array_split(a , 2)
print(b)
print(b[1])


