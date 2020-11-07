a = 1 
#help(a)

# The help function opens the doc string for the a object, in this case it tells
# us that a is an integer object.

#dir(a)

# The dir function lists all the attributes posses by an instance of the int
# class.

print(a.__abs__())

b = -2
print(b.__abs__())

# It is in very rare cases that you should actually call a dunder method in 
# python. You should instead make sure you use in the built-in function 
# instead which is abs() in this case 

print(abs(a))
print(abs(b))

# Example of List

# Remember lists are mutable. Also remember that a list isn't storing 
# 'Values' it is storing references. Which is why you can change names
# when indexing as shown below.

list1 = [ 1, 2, "Hello", 4, 5 ]
print(list1)
list1[2] = 3
print(list1)


# Example of Tuple

# Remember Tuple's are by design the immutable version of a list.
# You can convert a list to a tuple by using the tuple method. 

tuple1 = ( 1, 2, "Hello", 3, 4 )

# Example of Set

# The set type is supposed to be the equivilent of the math set type
# This means they are unordered containers of unique values. 
# There is a whole load of set mathematics surrounding this object
# for example Union, Intersection, Difference and so on... 
# There is a whole spiel about mutability and hashing on page 73 that is
# probably worth another read at some point. 

set1 = { 1, 2, "Hello", 3, 4 }

# Example of Dictionary
dir1 = {"key" : 1}

# Vertical split the iterm2 so that you have a terminal on the write
# and then open a python environment and play around with the 
# variables using the help() and dir() functions
