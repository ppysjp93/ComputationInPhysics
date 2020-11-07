import particle as p

class CompositeParticle(p.Particle):

    def __init__(self, parts):
        self.constituents = parts

