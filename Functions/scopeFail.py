 a = "A"


 def func():
     # you cannot use the global 'a' because...
     print("Big " + a) 
     # a local 'a' is eventually defined!
     a = "a"
     print("small " + a)

func()

# This function will cause an error because the 'a' is defined globally
# AND locally. The local 'a' is unbound until it is assigned the value "a"
# Since the local a is called in the Big print function before it is assigned
# there is an error. 
