# import the particle module
import particle as p

####################
# CLASS VARIABLES
####################

print(p.Particle.roar)

# This means we don't need an instance of a class to access one of its 
# attributes. We also don't have to say whether a class is static or not like
# we do have to in Java which is nice on some levels. 

higgs = p.Particle(0, 125, 0)

print("The higgs particle shouted: {0}".format(higgs.roar))
print("The mass of this particle is {0} GeV/c^2".format(higgs.m))

# A second way to gain access to one of the attributes of our Particle class
# is to make an instance of the particle (in this case the instance is a 
# higgs particle) and then call the attribute -> instance.attribute

# Roar is an instance of an attribute that is a "Universal" variable
# They are also known as "Class Variables" 


