import numpy as np

# a = np.array([1,2,3,4,5])
# print(a)
# a = np.append(a,[6,7])
# print(a)

# a = np.array([[1,2],[3,4]])
# print(a)
# a = np.append(a,[6,7])
# print(a)


# a = np.array([1,2,3,4,5])
# print(a)
# a = np.insert(a,1,[6,7])
# print(a)




# a = np.array([[1,2 ,3],[4,5,6]])
# print(a)
# a = np.insert(a,1,[7,8,9] , axis = 0)
# print(a)





a = np.array([[1,2 ,3],[4,5,6]])
print(a)
a = np.insert(a,1,[7,8,9] , axis = 0)
print(a)
print(np.delete(a,1 , axis = 1))