# a simple lambda
lambda x: x**2

# a lambda that is called after it is defined
(lambda x, y=10: 2*x +y)(42)

# just because it isi anonymous doesn't mean we can't give it a name!
f = lambda: [x**2 for x in range(10)]
print(f())

# a lambda as a dict value
d = {'null': lambda *args, **kwargs: None}

# lambda as a keyword argument f in another function
def func(vals, f=lambda x: sum(x)/len(x)):
    f(vals)
 
# a lambda as a keyword argument in a function call
func([6, 28, 496, 8128], lambda data: sum([x**2 for x in data]))

# lambda's are often used when sorting containers. We can adapt the sorted 
# built-in function so that there is a 'key-function' which is applied to 
# each element in the list. The sorting then occurs on the return value of 
# the 'key-function'

nums = [8128, 6, 496, 28]

sorted(nums)

sorted(nums, key=lambda x: x%13)
