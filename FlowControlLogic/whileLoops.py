# For while loops, while the condition is true it will keep on executing

t = 3 
while 0 < t:
    print("t-minus " + str(t))
    t = t - 1
print("blastoff!")

while False:
    print("I am sorry, Dave.")
print("I can't print that for you.")

# You can use the break statement in python to exit a loop early

fib = [1, 1]
while True:
    x = fib[-2] + fib[-1]
    if x%12 == 0:
        break
    fib.append(x)
print("The first 10 fibonaccie numbers are {0}".format(fib))

