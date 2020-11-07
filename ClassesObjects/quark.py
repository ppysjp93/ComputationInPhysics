import elementary as e
from fractions import Fraction

class Quark(e.ElementaryParticle):

    """ 
    Attributes
    - - - - - - 
    Quarks are ElementaryParticles which have Flavor and Color.
    Their comibined attributes are:
    charge, mass, position, spin, flavor and color.
    However Color hasn't been impolemented as of yet. 
    To initialise:
    Quark(charge,mass,position, spin, flavor) 
    """
    flavors = ["up", "down", "charm", "strange", "top", "bottom"]
    masses = [2.3, 4.8, 1.275*(10**3), 95, 173070, 4.18]
    charges = [2/3,-1/3]
    spin = 0.5
    
    @staticmethod
    def possible_flavors(): 
        return Quark.flavors 
    
    @staticmethod
    def possible_masses(): 
        return Quark.flavors 
    
    @staticmethod
    def possible_flavors(): 
        return Quark.flavors 

    def __init__(self, flavor):
        if flavor in Quark.flavors:
            self.f = flavor
        else:
            raise AttributeError(""" 
            The flavor must one of the possible flavors: {0}
            """.format(flavors))
         
        self.setchargemassspin(self.f)
        
    def myAttributes(self):
        print("""
        I am an {0} quark! I have a mass of {1} MeV/c^2, a charge of {2} and 
        a spin of {3}.
        """.format(self.f, self.m, self.c, self.s))


         
    def flip(self):
            if self.flavor == flavors[0]:
                 self.f = flavors[1]
            elif self.f == flavors[1]:
                 self.f = flavors[0]
            elif self.f == flavors[2]:
                 self.f = flavors[3]
            elif self.f == flavors[3]:
                 self.f = flavors[2]
            elif self.f == flavors[4]:
                 self.f = flavors[5]
            elif self.f == flavors[5]:
                 self.f = flavors[4]
            else:
                raise AttributeError("""
                The quark cannot be flipped because the flavor is not valid.
                """)
    
    def setchargemassspin(self,flavor):
            i = 0
            for f in Quark.flavors:
                if flavor == Quark.flavors[i]:
                   index = i
                   break
                i += 1 
                
            if index % 2 == 0:
                self.c = Quark.charges[0]
            else:
                self.c = Quark.charges[1]

            self.m = Quark.masses[index]
            self.s = Quark.spin            



up_quark = Quark("up")    
up_quark.myAttributes() 
down_quark = Quark("down")    
down_quark.myAttributes() 

