import pandas as pd
print("""
The data frame object can be thought of as a collection of series.

s = pd.Series([42, 43, 44],
        index=["electron",
                "proton",
                "neutron"])\n 
t = pd.Series({'electron': 6,
                'neutron': 28,
                'proton': 496,
                'neutrino': 8128})\n
df = pd.DataFrame({'S': s, 'T': t})
                """)

s = pd.Series([42, 43, 44],
        index=["electron",
                "proton",
                "neutron"]) 

t = pd.Series({'electron': 6,
                'neutron': 28,
                'proton': 496,
                'neutrino': 8128})

df = pd.DataFrame({'S': s, 'T': t})
print("\ndf = \n", str(df))

print("""
Data frames have many other operations that can be applied to them such as 
slicing, having rows removed. They have sophisticated indexing semantics 
in the way that Series do too. See below:""")
print("""
df[::2] Slices every other element.""")
print("\n = df[::2] \n", str(df[::2]))

print("""
You can append to a Data Frame:\n
dg = df.append(
        pd.DataFrame({'S': [-8128]},
            index=['antineutrino']))""")

dg = df.append(
        pd.DataFrame({'S': [-8128]},
            index=['antineutrino']))

print("\ndg = \n", str(dg))

print("""
dh = dg.drop('neutron')""")

dh = dg.drop('neutron')

print("\ndh = \n", str(dh))

print("""
You can also easily transpose a Data Frame df.T""")
print("\ndf.T =  \n", str(df.T))

print("""
You can also apply boolean arithmetic to data frames df < 42""")
m = df < 42
print("\nm = \n", str(m))

print("""
m is a boolean mask and is itself also a dataframe""")

print("""
Accessing a single column will return a series df['T']""")
print("\ndf['T'] = \n", str(df['T']))




