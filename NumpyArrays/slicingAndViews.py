import numpy as np
# Numpy arrays have the same slicing sematics as Python lists when it comes to
# accessing elements or subarrays.
print("\nSlicing and Views of Arrays\n")
a = np.arange(8)
print("a = " + str(a))
print("a[::-1] = " + str(a[::-1]))  
print("a[2:6] = " + str(a[2:6]))  
print("a[1::3] = " + str(a[1::3]))  

# For the case of a list of lists in python and you want to slice along 
# multiple aes, you have to slice the inner list for every element in the slice
# of the out list

# outer = [...]
# selection = [inner[a:b:c] for inner in outer[x:y:z]]
# Each inner is an innern list obviously. So this is saying slice each inner
# list in the outer list. Makes sense.
# The number of loops required for this then becomes the dimensions the list has
# minus 1

# Numpy is much more concise.
print("\n4x4 Matrix Example\n")
a = np.arange(16)
a.shape = (4,4)
print(a)
print()
print("Slice Even Rows and Odd Columns")
print("a[::2, 1::2] = \n" + str(a[::2, 1::2]))  
print()
print("Slice the inner 2x2 array")
print("a[1:3, 1:3] = \n" + str(a[1:3, 1:3]))  
print()
print("Reverse the first 3 rows, taking the first 3 columns")
print("a[2::-1, :3] = \n" + str(a[2::-1, :3]))  

# the most important thing to take from array slicing is that slices are views
# into the original array. No data is copied when a slice is made.
# This makes numpy  very fast.

print("\nBASE EXAMPLE")
a = np.arange(6)
print("a = "+ str(a))
b = a[1::2]
print("b = a[1::2]\n" + str(b))
print("Changing the element in b changes the element in a")
b[1] = 42
print("b[1] = 42\n a = " + str(a))  
print("b.base is a? " + str(b.base is a))

# If you truly want a copy of a slice of an array then you can always create
# a new array from the slice
print("\nREBASING")
a = np.arange(16)
print("a = " + str(a))
b = np.array(a[1::11])
print("b = np.array(a[1::11])\n b = " + str(b))
print("b.base is a? " + str(b.base is a))

print("\nVIEW EXAMPLE")
print("""We can view an int64 array as an int 32 array with twice as many 
elements for example""")

a = np.arange(6, dtype=np.int64)
print("a = np.arange(6, dtype=np.int64)\n" + str(a))
print("a.view('i4') = " + str(a.view('i4')))
