print()
# The technical syntax 
# for <loop-var> in <iterable>:
#     <for-block>
for t in [3, 2, 1]:
    print("t-minus " + str(t))
print("blastoff!")

print()
# This loop will only print the odd values because of the continue statement
for t in [7, 6, 5, 4, 3, 2, 1]:
    if t%2 == 0:
        continue
    print("t-minus " + str(t))
print("blastoff!")

print()
# String iteration produces each letter in tern
for letter in "Gorgus":
    print(letter)

print()
# Unordered Data structures like a set iteration in unordered
for x in {"Gorgus", 0, True}:
    print(x)

print()
# Looping over dictionaries is even more ambiguous because it could be 
# over the keys, values or both
d = {"first":"Albert","last":"Einstein","birthday":[1879, 3, 14]}
for key in d:
    print(key)
    print(d[key])
    print("=====")

print()
# More dictionaries
for key in d.keys():
    print(key)

print("\n=====\n")

print("Values:")
for value in d.values():
    print(value)

print("\n=====\n")

print("Items:")
for key, value in d.items():
    print(key, value)

# You can choose not to unpack the items in the dictionary in which case
# a list of tuples will be printed

print("\n=====\n")
print("In python the pattern for looping through an iterable is that the 
        variable name is the singular noun and the iterable is the corresponding 
            plural noun.")

print("\n=====\n")
quarks = {'up', 'down', 'top', 'bottom', 'charm', 'strange'}
for quark in quarks:
    print(quark)




