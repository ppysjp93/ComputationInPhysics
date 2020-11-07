def momentum_energy(m, v):
    p = m * v
    e = 0.5 * m * v**2
    return p, e

m = 42
v = 65
print("\n An object has a mass of {0} and a velocity of {1}.".format(m,v))

p_e = momentum_energy(42.0, 65.0)

print("""\n The mass and energy is calculated using the momentum energy function
which returns a tuple containing the momentum and energy: {0}""".format(p_e))

# unpack tuple
mom, eng = p_e
print("\n The momentum by itself is: {0}".format(mom))

