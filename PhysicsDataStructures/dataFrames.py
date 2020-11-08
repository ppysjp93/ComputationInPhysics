print("################################################################################") 
print("""
DATA FRAMES""")
print("################################################################################") 
 
print("""
The data frame is an abstraction of tables and structured arrays. Given a 
collection of 1D arrays, the data frame allows you to form complex relationships
between those arrays. A data frame is  made up of columns called 'series'. A 
series is essentially a Numpy array.""")

import pandas as pd

print("\nSERIES")

print("""
The series in pandas is essentially a numpy array with an optional associated 
index. """)

print("""
s = pd.Series([42, 43, 44], dtype='f8') """)
s = pd.Series([42, 43, 44], dtype='f8') 
print("\ns = \n", str(s))

print("""
We can name the indexes instead of having numbers for indexing.""")

print("""
s = pd.Series([42, 43, 44],
        index=["electron",
                "proton",
                "neutron") """)

s = pd.Series([42, 43, 44],
        index=["electron",
                "proton",
                "neutron"]) 

print("\ns = \n", str(s))

print("""
We can index into a series in a dict like fashion s['electron']:""")

electron = s['electron']

print("\nelectron = \n", str(electron))


print("""
We can also slice by indices to create a subseires because the index itself has
an order""")

print("\ns['electron':'proton'] = \n", str(s['electron':'proton']))

print("""
Normal integer indexing is also still ok. """)
print("\ns[1:] = \n", str(s[1:]))

print("""
We can also create a sereies by using a dictionary.\n
t = pd.Series({'electron': 6,
                'neutron': 28,
                'proton': 496,
                'neutrino': 8128})""")
                
t = pd.Series({'electron': 6,
                'neutron': 28,
                'proton': 496,
                'neutrino': 8128})

print("\nt = \n", str(t))

print("""
You can also perform arithmetic with series for example s + t. Since t has a 
value for the neutrino but s doesn't, the value associated with the neutrino
will be NaN.""")

print("\n = s + t\n", str(s + t))


