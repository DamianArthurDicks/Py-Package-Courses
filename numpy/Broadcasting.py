import numpy as np

#broadcasting
#allows numpy to perform arithmetic operations on arrays with different dimensions
#there are 2 rules with broadcasting:
#the number of rows or columns must be the same or == 1
#example:
array1 = np.array([[1], [2], [3], [4], [5]])
array2 = np.array([[1, 2, 3, 4, 5]])

#print(array1.shape)
#print(array2.shape)

print(array1 * array2)

