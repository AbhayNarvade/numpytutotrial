import numpy as np

# sort
# a = np.array([[7,6,14,11,1,5] , [2,1,81,66,44,5]])
# print(np.sort(a ))


# a = np.array([7,6,14,11,1,5] )
# print(np.where(a % 2 ==0))


# a= np.array([1,2,3,4,5,6])
# 
# print(np.searchsorted(a , 5))





# a= np.array([1,2,3,4,5,6])

# fa = [True , False , True , False , True , False]

# new = a[fa]

# print(new)


a= np.array([1,2,3,4,5,6])

fa = a % 2 == 0


new = a[fa]

print(new)