import numpy as np

print("""MASKING
A mask is like a fancy index, except that it must be a boolean array. Masks can
be applied to any array that has the same shape or the same length. A mask must 
be a numpy array of bools and like fancy indexing will produce another array.
""", end="\n")
print("EXAMPLE 1")
a = np.arange(9)
a.shape = (3,3)

# Create Mask
m = np.ones(3, dtype=bool)
print("a = ", end = 2*"\n")
print(a, end = 2*"\n")
print("The mask: m = np.ones(3, dtype=bool)")
print(m)
print()
print("Using the mask we can get the diagonal with a[m, m] =", end = 2*"\n")
print(a[m, m])

print()
print("EXAMPLE 2")
m =np.array([[1, 0, 1],
            [False, True, False],
            [0, 0, 1]], dtype=bool)
print(a[m])
print()
print("""You can also generate masks by doing comparisons. This gives an easy 
way of cleaning and munging data""")        
m = (a >= 7)
print("m = (a >= 7)", end = 2*"\n")
print("a[m] = ", end = 2*"\n")
print(a[m])
print()
print("The above can be simplified to a[a >= 7] which is very nice and concise.")
print(a[a >= 7])
print("Masks should be used in conjunction of Numpy's where() function")
print("The above should be a[np.where(a >= 7)] which is very nice and concise.")
print(a[np.where(a >= 7)])
print("""The where function always returns a tuple which means that it then can
be indexed like in the following example.""")
print(a[:,:])
print(a[:, np.where(a < 2)])
print("With indexing, this example is weird so probably worth another read.")
print(a[:, np.where(a < 2)[1]])



