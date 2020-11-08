print("######################################################################") 
print("""
HASH TABLES""")
print("######################################################################") 

print("""
Hash tables are everywhere in software development. The most common one that we
have use so far is the Python dictionary. This data structure is so important
that it forms the backbone of the Python language. So the question is how do 
hash tables work?
Hash tables are a mapping of keys to values where each key must be a unique 
value. The rows of the table are sorted according to hte hash of the key modulus
the length of the table. Missing or Empty rows are allowed. Hash function is 
used to generate the value of the key, python has the built in hash() function.
The main problems with hash tables arise when they run out of spae and you want
to add more items and what happens when two different keys produce the same 
hash?""")

print("\nRESIZING")

print("""
changing the length of a hash table changes the value of hash(key)%table_len. 
for example an object who has a hash value -4886380829903577079, if the original
table has a length of 8, then its hash-key is 1, whereas if the length of the 
table is doubled to 16 the hash-key has a new value of 9. The key thing to 
understand is that a resize of a hash-table does more than just copy it, it also
rearranges it. Users don't need to worry about resizing. What should concern 
them is how they insert into a hash table. Essentially one insertion that 
inserts many items is better than many insertions that insert one item because
this means the hash-table has to go through the resizing array only once which
takes less computation. In python this means you should update() dicts when 
possible rather than assigning new entries( d[key] = value ). Different hash 
tables have different approaches to when they should resize, whether that be 
the table is half, three quarters or completely full.""")

print("\nCOLLISIONS")

print("""
A hash colision is where a new key hashes to the same value as an existing key
in the table. Even though the space of hash values is huge, ranging from 
-9223372036854775808 to 9223372036854775807 on 64 bit systems, hash collisions
are more comomn than you would think. An empty string, and integer 0 a 
float of 0.0 and a False bool all hash to the same value. Collisions are an 
example of the birthday paradox which states that the likelihood two people 
share a birthday is much more likely than 2 people sharing a specific birthday.
(I don't see why this is a paradox anymore). Anyway this principle can be 
applied to hash tables and in python the number of slots in a dictionary is 
N = 2 ** 64 ~ 10 ** 20 however the likelihood of a colision in the hashtable 
occuring reaches 1 when the number of hashes is 10**10. So s/N tells us that
only a billionth of the table can be full for the likelihood of a collision 
occuring being equal to one. Which is counterintuitive hence the paradox.
Hash tables have incredible performance at the cost of being difficult to 
implement, however this shouldnt be a problem because most programming languages
have their own implemntations anyway.""")

print("\nDATA FRAMES")

print("""
these have already been discussed earlier on but essentially pandas uses the 
dataframe as its main object.  """)



