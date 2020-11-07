# Comprehensions are a way of making a Loop which is normally 3 lines into a 
# single line entity which means less typing. 

quarks = {'up', 'down', 'top', 'bottom', 'charm', 'strange'}
upper_quarks = []
for quark in quarks:
    upper_quarks.append(quark)

# as seen here this took three lines to type which is quite long

# There are three types of comprehensions List, Set and Dictionary

# The pattern for a List comprehension is as follows
#   [<expr> for <loop-var> in <iterable>]

# The pattern for a Set comprehension is as follows
#   {<expr> for <loop-var> in <iterable>}
# Notice hte change in parenthesese here

# Dictionary Comprehension is a slight variation
#   {<key-expr>: <value-expr> for <loop-var> in <iterable}
 
print("\n-----------------------------")
print("List Comprehension Example")
print("-----------------------------")
print(quarks)
upper_quarks = [quark.upper() for quark in quarks]
print(upper_quarks)


print("\n-----------------------------")
print("Set Comprehension Example")
print("-----------------------------")
print("""\nYou can use a Set comprehension to normalise entry data that is 
categorical so that you know the unique entries are and have them all 
the same\n""")

entries = ['top', 'CHARm', 'Top', 'sTraNGe', 'strangE', 'top']
quarks = {quark.lower() for quark in entries}
print(entries)
print(quarks)

print("\n-----------------------------")
print("Dictionary Comprehension Example")
print("-----------------------------")
print("""\nYou can use a dictionary comprehension on a list to create a dictionary
which maps input to a result. A verrrry nice featur \n""")

entries = [ 1, 10, 12.5, 65, 88 ]
results = {x: x**2 + 42 for x in entries}


print("\n-----------------------------")
print("Comprehension Example with Condition")
print("-----------------------------")
print("""\n You could also compute the set of squares of Fibonaccie
        numbers but only where the Fibonnacci number is divisible by five.""")


fib = [1, 1]
while True:
    x = fib[-2] + fib[-1]
    if x%12 == 0:
        break
    fib.append(x)
print("The first 10 fibonaccie numbers are {0}".format(fib))

print({x:x**2 for x in fib if x%5==0})


