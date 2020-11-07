def sagan():
    quote = "With insufficient data it is easy to go wrong."

def null():
    pass

# Define the function
def forty_two():
    return 42

# call the function 
forty_two()

# call the funtion and print the result
print("The meaning of life is " + str(forty_two()))

# call the function, assign the result
# to x, and print x
x = forty_two()
print(x)
print(x)

def forty_two_or_bust(x):
    if x:
        print(42)
    else:
        print(0)

# call the function
forty_two_or_bust(True)

bust = False
forty_two_or_bust(bust)
a = 3

# Doc Strings are used to explain what a function does briefly
# and it's usage in particular how to use the positional arguments
def power(base,x):
    '''\n\nComputes base^x. Both base and x should be integers, floats,
    or another numeric type.'''
    return base**x

print("""\nTo view the docstring of a function use the __doc__ attribute of the 
object""" + power.__doc__)

from math import sin

def sin_inv_x(x):
    if x == 0.0:
        result = 0.0
    else:
        result = sin(1.0/x)
    return result


