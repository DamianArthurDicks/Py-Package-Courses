#Aggregate functions = summarize data and typically return a single value

import numpy as np

array = np.array([[1, 2, 3, 4, 5], 
                  [6, 7, 8, 9, 10]])

#returns the sum of the array
print(np.sum(array))

#returns the mean of the array
print(np.mean(array))

#returns the standard deviation of the array
print(np.std(array))

#returns the variant of the array
print(np.var(array))

#returns the minimum value of the array
print(np.min(array))

#returns the maximum value of the array
print(np.max(array))

#returns the index of the minimum value in the array
print(np.argmin(array))

#returns the index of the maximum value of the array
print(np.argmax(array))

#returns the sum of the columns in the array
print(np.sum(array, axis=0))

#returns the sum of the rows in the array
print(np.sum(array, axis=1))