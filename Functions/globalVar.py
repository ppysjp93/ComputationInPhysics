 a = "A" 

 def func():
     global a
     print("Big " + a)
     a = "a"
     print("small " + a)

func()
print("global " + a)

# The global key word is like static typing, it let's everyone know exactly
# which version of a we are focusing on. A side effect of this is that 
# if a is then reassigned in the function, then this is globally the case too. 
