print("################################################################################") 
print("""
B-TREES""")
print("################################################################################") 

print("""
B-trees are one of the most common data structures for searching over big chunks
of data, which makes them very useful for databases.""")

print("""
\t        .--.-----------[5  89]-------.
\t       /   |                         |
\t[1 2 3]  [21]            .----.--[233 1597]--.
\t        /   \           /     |              |
\t    [8 13]  [34 55] [144] [377 610 987] [2584 4181]""")

print("""
Each node in a b-tree can store many values (it could be an entire table for 
example). In the case where a Binary Search tree can only contain a single value
the B-tree becomes a binary search tree (bot to be confused with a binary tree.
\n
\t       [5]
\t       / \ 
\t    [2]  [8]
\t   /  \ 
\t [1]  [3]    """)

print("""
B-trees can be 'rotated' and still have the same search properties. It has a 
a different structure but its order is still the same and it still searches the 
same.
\n
\t      [2]
\t     /   \ 
\t   [1]   [5] 
\t        /   \ 
\t      [3]   [8] """)  

print("""
B-trees are very effective for organizing array data in a non-linear fashion.
The index of the array determines on which node in hte tree the array lives. 
The tree itself manages the locations of all of the nodes. The nodes manage the
data chunks assigned to them.
In practice B-trees follow a set of simple rules as a way of reaping the 
performance benefits and making the logic easier to understand.
\n* The height of the tree is constant. All leaves exist at the same height.
\n* The root node has height 0.
\n* The maximum number of child node, m, is kept below a constant number across
    all nodes.
\n* Nodes should be split as evenly as possible over the tree in order to be 
    'balanced'.""")

# To see the following B-list in action you are going to need to set up some 
# pyenvs, something I'm not willing to do currently

#import blist

#b = sorteddict(first="Albert",
#                last="Einstein", 
#                birthday=[1879, 3, 14])
#              


#b['died'] = [1995, 4, 18]

#klist(b.keys()) 

