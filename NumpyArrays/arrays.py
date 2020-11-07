import numpy as np
print()
# Common types of arrays
print("Common types of arrrays")
print(np.array([6, 28, 496, 8128]))
print(np.arange(6))
print(np.zeros(6))
print(np.ones((2, 3)))
print(np.empty(4))
print()

# Linspace
print("Lin/Log:space")
print(np.linspace(1, 2, 5))
print(np.logspace(1, -1, 3))
print()

# Reshaping an array
print("Reshaping arrays")
a = np.arange(4)
print(a)
a.shape = (2,2)
print(a)

# One of the central patterns of Nupy: operations that involve attributes  or 
# methods of ndarray occur in-place, while functions that take an ndarray as an
# argument return a modified copy

# Knowing the dtype is very important, there is a list in the book. 
# The dtype tells us how much space is taken by each element in the array
print("\nDataTypes")
a = np.array([6, 28.0, 496, 8128], dtype=np.int8)
print(a)
print(a.dtype)

b = np.array([6, 28.0, 496,8128])
print(b)
print(b.dtype)

print("\nFlexibleDataTypes")
print(np.array(['I will have length six', 'and so will I!'], dtype='S6'))
print("The data type setting has stopped the printing of the entire strings")
