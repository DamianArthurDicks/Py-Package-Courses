import numpy as np

#random number generator
#seed generates the same multidimensional/singular array every time executed
rng = np.random.default_rng(seed=1)
#print(rng.integers(low=1, high=101, size=(3, 2)))

#seed for uniform method 
np.random.seed(seed=1)
#gives every number genearted the same chance of being generated
#print(np.random.uniform(low=-1, high=1, size=(3, 2)))

#shuffles the array
array = np.array([1, 2, 3, 4, 5])
rng.shuffle(array)
#print(array)

#generates a random choice
fruits = np.array(["apple", "banana", "orange", "coconut", "pineapple"])
fruits = rng.choice(fruits, size=2)
print(fruits)