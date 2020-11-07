# Pythons max function will take any number of arguments and still return a 
# a value

max(6,2)                    # --> [6]
max(6,42)                   # --> [42]
max(1, 16,12)               # --> [16]
max(65, 42, 2, 8)           # --> [65]

# To create your own special function that contains a variable number of args
# you must prefix the argument with an asterix *. It must also be the last 
# argument that is defined by the function

def minimum(*args):
    """Takes any number of arguments!"""
    m = args[0]
    for x in args[1:]:
        if x < m:
            m = x
    return m

# The *args variable is a tuple, which means it is immutable, hashable, and 
# can have duplicate elements.

minimum(6,42)                    # --> [6]
data = [65, 42, 2, 8]
print("The minimum of {0} is {1}".format(data,minimum(*data)))

# Variable number of keyword arguments
# The kwargs variable is a dictionary, which means it is mutlable and 
# therefore not hashable. hmm...
def blender(*args, **kwargs):
  """Will it?""" 
  print(args, kwargs)


blender("yes", 42)                          # --> ('yes', 42) {} 
blender(z=6, x=42)                          # --> () {'x' : 42, 'z': 6} 
blender("no", [1], "yes", z=6, x=42)        # --> ("no", [1], "yes")  {'x' : 42, 'z': 6} 

t = ("no",)
d = {"mom": "ionic"}
blender("yes", kid="covalent", *t, **d)     # --> ('yes', 'no') {'mom': 'ionic',
                                            # 'kid': 'coalent'}

# The last blender example demondatrates that all tuple arguments will be merged
# together and all dictionary arguments will be merged together. 
