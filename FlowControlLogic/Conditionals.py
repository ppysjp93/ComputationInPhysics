h_bar = 1.0

if h_bar == 1.0:
    print("h-bar isn't really unity! Resetting ..")
    h_bar = 1.05457173e-34

x = 0 

if x == 0:
    y = 0
else:
    y = sin(1/x)

print("The value of y is {0}".format(y)) 


# condition?x:y Construct in Python below

h_bar = 1.05457173e-34 if h_bar == 1.0 else h_bar


