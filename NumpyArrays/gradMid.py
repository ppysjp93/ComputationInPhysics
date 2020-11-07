import numpy as np 

print("\nPERFORMING DERIVATIVE\n")

print("""The only problem with this method is the length of the gradient and
midpoint arrays are one less than the original arrays.""")         

a = np.arange(10, 20)
b = np.arange(20, 30)
a = np.array(a ** 2)
print("The points in x and y are bin boundaries in this case")
print("y = " + str(a))
print("x = " + str(b))
print()
print("y[1:] = " + str(a[1:])) # From 11 - 19 
print("y[:-1] = " + str(a[:-1])) # From 10 - 18
print()
print("x[1:] = " + str(b[1:])) # From 21 - 29 
print("x[:-1] = " + str(b[:-1])) # From 20 - 28 
print()
print("(y[1:] - y[:-1]) / (x[1:] - x[:-1]) = ")
gradient = (a[1:] - a[:-1]) / (b[1:] - b[:-1]) 
print(gradient)
print("The gradient for the midpoint of the bin is given above")
print("midpoint = (x[1:] + x[:-1])/2")
midpoint = np.array((b[1:] + b[:-1])/2)
print(midpoint)
print()
print("""Exercise: Create a function that takes two arrays and returns, the
the corresponding gradient and midpoint arrays""")

def gradMid(x, y):
    """
    Takes two numpy arrays which act as bin boundaries of the same length and 
    returns gradient and midpoints of each bin, numpy arrays with a length one 
    less of the original arrays.
    """
    gradient = (y[1:] - y[:-1]) / (x[1:] - x[:-1]) 
    midpoint = np.array((x[1:] + x[:-1])/2)
    return (gradient, midpoint)

x = np.arange(0, 20, 1)
y = np.arange(0, 40, 2)

gradient, midpoint = gradMid(x, y)
print("gradient = \n" + str(gradient))
print("midpoint = \n" + str(midpoint))

