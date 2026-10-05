#arrays

import numpy as np

array = np.array([1, 2, 3, 4])

array = array * 2

#multi-dimensional array
#it behaves in a sequence each array must contain the same number of items, columns and rows
md_array = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                     [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
                     [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])

sum = md_array[0, 1, 1] + md_array[2, 0, 1] + md_array[2, 2, 0]

#print(array)

#".ndim" counts the number of dimensions in the multi-dimensional array
#print(md_array.ndim)

#".shape" counts the number of depth, columns and rows
#print(md_array.shape)

#multidimensional indexing, it is used to index through multidimensional arrays(faster than chain indexing)
#md_array[depth, row, column]
#print(md_array[0, 0, 0])
#print(sum)

#slicing a multidimensional array
#md_array[start:end:step]
#print(md_array[0:10:2])