import numpy as np 

print("\nBROADCASTING EXAMPLE 1\n")
a = np.arange(4)
a.shape = (2, 2)

b = np.array([[42], [43]])
print("\nEXAMPLE 1")
print("a = \n" + str(a))
print("b = \n" + str(b))
print("Numpy Default Multiplication is broadcasting multiplication") 
print("a * b =\n " + str(a * b) ) 
print()
print("""There are compatibility rules for arrays of different shapes if you are
going to perform""", end='\n * ')
print("For each axis the dimensions are equal (a.shape[i] == b.shape[i])", end = "\n\t")
print("or the dimension of one is 1 (a.shape[i] == 1 or b.shape[i] == 1)")
print("The rank (number of dimensions) of one is less than that of ", end = "\n\t")
print("the other (a.ndim < i or b.ndim < i).")
print("In the above example every column of a is multiplied element wise by")
print("the values in b.")
print()
print("In order to perform the scalar product you must use the dot operator.")
print("np.dot(a, b)")

print("\nEXAMPLE 2")
a = np.arange(12)
a.shape = (4, 3)
b = np.array([16, 17, 18])
print("a = \n" + str(a))
print("b = \n" + str(b))
print("a + b" + str(a + b))
print(a.ndim)
print(b.ndim)

print("If we transpose the a then the dimensions don't fit for broadcasting")
print("test this out by uncommenting the code in the file, line 38")
a.shape = (3, 4) # Transpose is just swapping dimensions
print("a = \n" + str(a))

a = np.arange(16)
a.shape = (2, 2, 2, 2)
print("a = ", end = "\n ")
print(a)
b = np.arange(2)
b.shape = (2, 1) # EXERCISE: Reshape B and see it's effects, it's interesting!
print("b = ", end = "\n ")
print(b)
print("c = ", end = "\n ")
print(a + b)

print("\nFinally you can add 'fake' dimensions by using the newaxis property for")
print("numpy. The max number of dimensions handled this way is 32 before numpy's")
print("brain begins to melt. To do this use the np.newaxis property.")

a = np.arange(6)
a.shape = (2, 3)
b = np.array([2, 3])

print(b[:, np.newaxis] -a)


