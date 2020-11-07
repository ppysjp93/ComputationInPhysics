val = 0.0

try:
    inv = 1.0 / val
except ZeroDivisionError:
    print("A bad value was submitted {0}, please try again".format(val))


try:
    inv = 1.0 / val
except ZeroDivisionError:
    print("A zero value was submitted, please try again")
except:
    print("A bad value was submitted {0}, please try again".format(val))

if val == 0.0:
    raise ZeroDivisionError
inv = 1.0 / val     # This line will never run because the exception is raised
