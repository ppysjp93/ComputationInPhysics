# global scope
a = 6 
b = 42

def func(x, y):
    # local scope
    z = 16
    return a*y + b*y + z

# global scope
c = func(1, 5)

# Funtions are first class objects in python which means that they have two
# important features:

# 1) They may be dynamically renamed, line any other object.
# 2) Function definitions may be nested inside of other function bodies.

# global scope
a = 6
b = 42

def outer(m, n):
    # outer's scope
    p = 10

    def inner(x, y):
        # inner's scope
        return a*p*x + b*n*y
    
    # outer's scope
    return inner(m+1, n+1)

# global scope
c = outer(1, 5)
print("\nThe value of the inner funtion is {0}".format(c))

# x = m+1, y = n + 1 
# x = 2  , y = 6

# a*p*x = 6*10*2 = 120, b*n*y = 42*5*6 = 1260
# a*p*x + b*n*y = 1380

# Another example

a = 6                   # set the global vlaue of 'a'

def a_global():
    print(a)

def a_local():
    a = 42 
    print(a)

a_global()
a_local()
print(a)



