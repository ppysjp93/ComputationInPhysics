import numpy as np
print("FANCY INDEXING")
print("""Fancy indexing is great because it is much more flexible than slicing
or using the newaxis property. The cost is that it requires copying the data
to a new block of memory.\nBENEFITS\n*""")
print('You can provide arbitrary indices.' , end = '\n* ')
print('You can have repeated indices.', end = '\n* ')
print('Indices may be out of order.', end = '\n* ')
print('The shape of the index does not need to match the shape of the array.', end = '\n* ')
print('The shape of the index may have more or few dimensions than the array.', end = '\n* ')
print('Indices may be used seamlessly with slices.', end = 2*'\n')

print('EXAMPLE 1', end = '\n')
a = 2*np.arange(8)**2 + 1
print('2*np.arange(8)**2 + 1 = ' + str(a))
print('pull out the fourth, last and second indices = a[[3, -1, 1]]', end = '\n')
print(a[[3, -1, 1]])
print("Pull out the Fibonacci sequence")
fib = np.array([0, 1, 1, 2, 3, 5])
print("fib = np.array([0, 1, 1, 2, 3, 5])")
print(a[fib], end =2*"\n")
print('EXAMPLE 2', end = '\n')
print('Mixing slicing and fancy indexing can be done as long as it either one')
print('or the other that is done a long an axis. They should NOT be mixed.')
a = np.arange(16) -8
a.shape = (4, 4)
print('a = \n', str(a))
print('print out the third, last and first columns a[:, [2, -1, 0]]')
print(a[:, [2, -1, 0]], end = 2*"\n")
fib = np.array([0, 1, 1, 2, 3])
print("""Pull out a Fibonacci sequnce of row for every other column, starting 
from the back = a[fib, ::-2]. Note how the first dimension is fancy indexed
and the second dimension is sliced. Nice and efficient :)""")
print(a[fib, ::-2], end = 2*"\n")
print("""Get the digonal by using a range i = np.arange(4) -> a[i, i]""")
i = np.arange(4)
print(a[i, i])
print("""Lower diagonal by subtracting one to part of the range
 = a[i[1:], i[1:] -1 ]""")
i = np.arange(4)
print(a[i[1:], i[1:] -1])
print("""Upper diagonal by adding one to part of the range
 = a[i[1:], i[1:] + 1]""")
i = np.arange(4)
print(a[i[1:], i[1:] -1])
print("""Anti diagonal by reversal = a[i, i[::-1]]""")
print(a[i, i[::-1]])

