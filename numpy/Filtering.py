#Filtering
#filters out certain elements met under a condition in an array
#and creates a new array with the elements that haven't been filtered out

import numpy as np

ages = np.array([[17, 21, 32, 16, 19], 
                 [15, 38, 14, 24, 36]])

#teenagers are ages less than 18
#returns a single array without any dimensions
teenagers = ages[ages < 18]

#adults are ages greater than or equal to 18 and below 65
#use "&" instead of "and"/use "|" instead of "or" because numpy is programmed in C
adults = ages[(ages >= 18) & (ages < 65)]
print(teenagers)
print(adults)