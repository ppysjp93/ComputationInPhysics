# This programm doesn't work yet, but when we learn about inheritance
# we should be able to use inheritance to create  a Quark class and
# make this model work.


# import the class 
from quark import Quark

# create a Quark object
t = Quark()

# set the flavor
t.flavor = "top"

# flip the flavor
t.flip()

# print the flavor
print(t.flavor)

def flip(self):
    if self.flavor == "up":
        self.flavor = "down"
    elif self.flavor == "down":
        self.flavor = "up"
    elif self.flavor == "top"
        self.flavor == "bottom"
    elif self.flavor == "bottom"
        self.flavor = "top"
    elif self.flavor = "charm"
        self.flavor = "strange"
    elif self.flavor = "strange"
        self.flavor = "charm"
    
