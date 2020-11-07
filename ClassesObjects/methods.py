from scipy import constants

import particle as p

m_p = constants.m_p
r_p = {'x': 1, 'y': 1, 'z': 53}
a_p = p.Particle(1, m_p, r_p)
a_p.hear_me()
