def countdown():
    yield 3
    yield 2
    yield 1
    yield 'Blast off!'

# generator
g = countdown()
next(g)
x = next(g)
print(x)
y, z = next(g), next(g)
print(z)

for t in countdown():
    if isinstance(t, int):
        message = "T-" + str(t)
    else:
        message = t
    print(message)

# A more complex example could be creating a generator that finds the 
# the square of a range of values up to n and adds one to each one.

def square_plus_1(n):
    for x in range(n):
        x2 = x * x 
        yield x2 + 1 
    
for sp1 in square_plus_1(10):
    print(sp1)

# This is a good example of abstraction that has been used to tidy the
# complexities of the function away.

# PALINDROME GENERATOR
# You can create a palindrom generator that makes use of two sub generators
# the first yields all the values forwards and the second yields all the values
# backwards.

# This is the generic definition of the sub generator
def yield_all(x):
    for i in x:
        yield i

# paindrom using 'yield from' semantics which is more concise

def palindromise(x):
    yield from yield_all(x)         # yields forwards
    yield from yield_all(x[::-1])   # yields backwards

for letter in palindromise("hello"):
    print(letter, end = "")

# The above is equivalent to this full expansion:
def palindromize_explicit(x):
    for i in x:
        yield i
    for i in x[::-1]:
        yield i

print("\n")

for letter in palindromize_explicit("olleh"):
    print(letter, end = "")
