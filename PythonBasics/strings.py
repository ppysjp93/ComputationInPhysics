quote = ("Science is what we undertand well enough to explain to a computer. "
         "Art is everything else we do. "
         "-Donal Knuth")

x = "It's easy!"
y = 'The computer said, "Does not compute."'
z = "Bones said, \"He\'s daed, Jim.\""

# There are three types of string prefixes
# r - returns a raw string -> r"escape!\n" will print the "\" and the "n"
# b - creates a byte array -> b"this bytes"
# u - creates a unicode string -> "u"Rene Descartes"

# Multi-Line Strings

"""Humpty, he sat on a wall,
Then Humpty, he had a great fall.
But all the king's horses
And men with their forces
Couln't render his entrobpy small
"""

a = 42
b = 65.0

# Using formatting is easier and less clunky
# as it means you don't have to use string concatenations
# to get the behaviour that you desire.

"x={0} y={1}".format(x,y)

"x=" + str(x) + " y=" + str(y)
