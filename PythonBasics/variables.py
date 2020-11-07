h_bar = 1.05457e-34

# Variables that start with numbers are not allowed!
# 2plus_40 = 42 -> bad
two_plus40 = 42 # good :)

pi = 3.14159

h = 2 * pi * h_bar
print(h)

dims = 3                    # int, only digits
ndim = 3.0                  # float, because of the '.'
h_bar = 1.05457e-34         # str, quotes surround the text
label = "Energy (in MeV)"   # str, quotes surround the text


print(type("The type of h_bar is " + str(h_bar) + "\n"))

