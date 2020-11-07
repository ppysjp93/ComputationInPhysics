import particle as p

class ElementaryParticle(p.Particle):
    """ 
    Attributes
    - - - - - - 
    An elementary particle has no distinct constituent particles.
    However they do have an intrinsic angular momentum called spin.
    Based on there spin they are either fermions or bosons
    """
    
    def __init__(self, spin):
        self.s = spin
        self.is_fermion = bool(spin % 1)
        self.is_boson = not self.is_fermion

    def spin():
        return self.s
