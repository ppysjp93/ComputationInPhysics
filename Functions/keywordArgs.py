# This is a way of having default values that will be used for the arguments
# when value is called. 
def line(x, a=1.0, b=0.0):
    return a*x + b

line(42)                # no keyword args, returns 1*42 + 0
line(42,2)              # a=2, returns 84
line(42, b=10)          # b = 10, returns 52
line(42, b=10, a=2)     # returns 94 
line(42, a=2, b=10)

# MUTABLE DATA TYPES SHOULD NEVER BE USED AS DEFAULT VALUES
# THIS IS BECAUSE THEY RETAIN THEIR VALUE FROM ONE CALL TO THE NEXT.

# Do not do this! 
# In this scenario we have a function that takes a list and then appends a 
# a value to it. The list should keep growing, it should be new every time.

print("\n-------------------------------------------------")
print("Mutable Datatype Default Keyword Argument Problem")
print("-------------------------------------------------")
def myappend(x, lyst=[]):
    lyst.append(x)
    print(lyst)
    return(lyst)

myappend(6)            # seems right       -> [6]
myappend(42)           # hmm...            -> [6, 42]
myappend(12, [1, 16])  #                   -> [1, 16, 12]
myappend(65)           # nope, not right   -> [6, 42, 65]

# To get around this problem a common tactic is to set the mutable data type
# to have a default value of None and if the function is called without the 
# a value for the mutable type a new version of it is created as follows.

print("\n---------------------------------------------")
print("Mutable Datatype Default Keyword Argument Fix")
print("---------------------------------------------")

def myappend(x, lyst=None):
    if lyst is None:
        lyst = []
    lyst.append(x)
    print(lyst)
    return(lyst)

myappend(6)            # seems right       -> [6]
myappend(42)           # hmm...            -> [42]
myappend(12, [1, 16])  #                   -> [1, 16, 12]
myappend(65)           # nope, not right   -> [ 65]
