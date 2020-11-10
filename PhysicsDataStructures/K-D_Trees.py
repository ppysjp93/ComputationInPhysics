print("################################################################################") 
print("""
K-D TREES""")
print("################################################################################") 

print("""
A k-d tree is another tree data structure. This one excels at finding the 
nearest neighbor for points in a k-dimensional space. This is extraodinarily 
useful for many physics calculations. Often times, when solving geometric 
partial differential equations, the effect that matter the most in the volume at 
hand come from the directly surrounding cells. Splitting up the problem geometry
into a k-d tree can make it much faster to find the nearest neighbor cells.""")

print("""
The big idea behind k-d trees is that any point defines a k-1 dimensional 
hyperplane that partitons the remaining space into two sections. For example
in 1D a point p on a line l will split up the line into the space above p and 
the space below p. In two dimensions, a line will split up a box. In three 
dimensions, a plane will split a cube and so on. The points in a k-d tree can 
then be placed into a structure similar to a binary tree. The difference here is
that sorting is based on the point itself along an axis a and that a is equal
to the depth level of the point modulo the number dimension, k. Thus, a 
effectively defines an orientation for how points should partition the space.""")

print("""
K-d trees are not often modified once they are instantiated. Tehy typically have
get or query methods but do not have insert of delete methods. The structure of
space is what it is, and if you want to restructure space you should create a whole 
new tree. For n points, k-d trees are order log(n) on average for all of their
operations. In the worst case, they are order n.""")

print("""
K-d trees are most effective when k is small, which is perfect for physics where
for most calculations k is typically 3 and rarely goes above 6. Below is an 
example where k=2""")

print("\nEXAMPLE")

print("""
class Node(object): (1)

    def __init__(self, point, left=None, right=None): (2)
        self.point = point
        self.left = left
        self.right = right

    def __repr__(self): (3)
        isleaf = self.left is none and self.right is none
        s = repr(self.point)
        if not isleaf:
            s = "[" + s + ":"
        if self.left is not none:
            s += "\\n left = " + "\\n ".join(repr(self.left).split('\\n'))
        if self.right is not none:
            s += "\\n right = " + "\\n ".join(repr(self.right).split('\\n'))
        if not isleaf:
            s += "\\n ]"
        return s""")

print("""
def kdtree(points, depth=0): (4)
    if len(points) ==0:
        return None
    k = len(points[0])
    a = depth % k
    points = sorted(points, key=lambda x: x[a])
    i = int(len(points) / 2) # middle index, rounded down
    node_left = kdtree(points[:i], depth + 1)
    node_right = kdtree(points[i+1:], depth + 1)
    node = Node(points[i], node_left, node_right)
    return node""")

print("""
(1) A tree consists of nodes\n
(2) A node is defined by its point. Since this is a binary search tree, it may
    have one node to the left and one node to the right.\n
(3) A string representation of the node given its relative location on the tree.\n
(4) A recusive function that returns the root node given a list of points. This
    will automaticcaly be balanced.""")
    
class Node(object):

    def __init__(self, point, left=None, right=None):
        self.point = point
        self.left = left
        self.right = right

    def __repr__(self):
        isleaf = self.left is None and self.right is None
        s = repr(self.point)
        if not isleaf:
            s = "[" + s + ":"
        if self.left is not None:
            s += "\n left " + "\n ".join(repr(self.left).split('\n'))
        if self.right is not None:
            s += "\n right " + "\n ".join(repr(self.right).split('\n'))
        if not isleaf:
            s += "\n ]"
        return s

def kdtree(points, depth=0):
    if len(points) == 0:
        return None
    k = len(points[0])
    a = depth % k
    points = sorted(points, key=lambda x: x[a]) # need to revise lambdas
    # and how to doe sorting so will focus on sorting today.
    i = int(len(points) / 2)  # middle index, rounded down
    node_left = kdtree(points[:i], depth + 1) # recursion example
    node_right = kdtree(points[i+1:], depth + 1)
    node = Node(points[i], node_left, node_right)
    return node
