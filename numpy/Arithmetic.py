#Arithmetic

import numpy as np

#Scalar Arithmetic
#scalar -> single value(only has magnitude and no direction)
array = np.array([1, 2, 3])

#print(array + 1)
#print(array - 2)
#print(array * 3)
#print(array / 4)
#print(array ** 5)

#Vectorized Math Functions
#Vector -> single dimension(has magnitude and direction)
#math functions and constants you can apply to an array without looping
#square root
#print(np.sqrt(array))
#rounded to closest value
#print(np.round(array))
#round down
#print(np.floor(array))
#round up
#print(np.ceil(array))
#value of pi
#print(np.pi)

#exercise(includes both scalar and vector arithmetic)
#this calculates the area of a circle
#each radius is multiplied by pi and raised to the power of 2 
#scalar = "2"
#vector = "radii"
radii = np.array([1, 2, 3])
#print(np.pi * radii ** 2)

#Element-Wise Arithmetic
#applying arithmetic operations between 2 elements(arrays)
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
#print(array1 + array2)
#print(array1 - array2)
#print(array1 * array2)
#print(array1 / array2)
#print(array1 ** array2)

#comparison operators
#applying comparison operators to return a boolean value
scores = np.array([63, 75, 82, 94, 100])
#print(scores < 60)
#print(scores > 60)
#print(scores == 100)

#filtering numbers less than or equal to 74
#scores[scores <= 74] = 0
#print(scores)