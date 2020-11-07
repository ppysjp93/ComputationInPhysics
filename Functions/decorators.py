def null(f):
    """Always return None."""
    return 

def identity(f):
    """Return the function."""
    return f

def self_referential(f):
    """Return the decorator."""
    return self_referential

# There are two syntaxes for using decorators
# The first uses the '@' symbol and is a much more concise syntax
# However you can only use this syntax whilst you are defining the function
# that is being decorated.  

@null
def nargs(*args,**kwargs):
    return len(args) + len(kwargs)

# The second reassigns the function we want to decorate 
# to itself being called by the decorator

def nargs(*args,**kwargs):
    return len(args) + len(kwargs)
nargs = null(nargs)

# Say there is a function where we want to manipulate what it returns
# or its arguments. The method for doing this is by defining a wrapper function
# which typically will call the original function, and then perform the 
# modifications we want. An example is given below: 

def plus1(f):
    def wrapper(*args, **kwargs):
        return f(*args,**kwargs) + 1
    return wrapper

# This is incredibly powerful tool, as it allows us to change the output of a
# function so that it returns the same value plus 1. Below is an example
# of where we could use this decorator! 

@plus1
def power(base,x):
    return base**x

base = 4
x = 2 
print("""{0} to the power of {1} plus 1 equals {2}""".format(base, x, power(base,x)))

# You can also chain decorators 

@plus1
@identity
@plus1
@plus1
def root(x):
    return x**0.5

print(root(4))


# The final and most complex thing you will come across with decorators is the 
# decorator factory which allows you to paremetrize the decorator so that it 
# can be used multiple times without having to write it out again and again...

def plus_n(n):
    def dec(f):
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs) + n
        return wrapper
    return dec

# Decorator factories must return a decorator

@plus_n(6)
def root(x)
    return x**0.5



