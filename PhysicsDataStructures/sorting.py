print("################################################################################") 
print("""
https://docs.python.org/3/howto/sorting.html 
SORTINGHOWTO""")
print("################################################################################") 

print("""
Python lists have a built in list.sort() method that modifies the list 
in-place. There is also a sorted() built-n function that builds a new sorted
list from an interable below are some examples""")

print("\nEXAMPLE 1")

print("""
sorted([5, 2, 3, 1, 4])""")
print(sorted([5, 2, 3, 1, 4]))

print("\nEXAMPLE 2")

print("""
You can also use the list.sort() method. It modifies the list in-place (and 
returns  None to avoid confusion). Usually it's less convenient that sorted() -
but if you don't need the original list, it's slightly more efficient.""")

print("""
a = [5, 2, 3, 1, 4] 
a.sort()""")

a = [5, 2, 3, 1, 4] 
a.sort()
print("a = ", str(a))

print("\nEXAMPLE 3 ")

print("""
Another difference is that the list.sort() method is only defined for lists.
In contrast, the sorted() function accepts any interable.""")

print("""
sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})""")
print(sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}))

print("\nKEY FUNCTIONS")

print("""
Both list.sort() and sorted() have a key parameter to specify a funciton (or 
other callable) to be called on each list element pripor to making comparasions.
For example, here's a case insensitive string comparison:
\nsorted("This is a test string from Sam".split(), key=str.lower)\n""")
print(sorted("This is a test string from Sam".split(), key=str.lower))

print("""
The value of the key parameter should be a function or (other) callable) that
takes a single argument and retuns a key to use for sorting purposes. This 
technique is fast because the key fuciton is called exactly once for each input
record.
A common pattern is to sort complex objects using some of the object's indices
as keys.""")

print("\nEXAMPLE 1 ")

print("""
student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'C', 10)]""")


student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'C', 10)]

print("""
sorted_student_tuples = sorted(student_tuples, key=lambda student: student[2])
The 2 index makes sure we are sorting by age.""")
sorted_student_tuples = sorted(student_tuples, key=lambda student: student[2])
print("\nsorted_student_tuples = \n", str(sorted_student_tuples))

print("\nEXAMPLE 2")

print("""
The same technique works for objects with named attributes:  """)


print("""
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self. age = age

    def __repr__(self):
        return repr((self.name, self,grade, self.age))""")


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self. age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))

print("""
student_objects = [
        Student('john', 'A', 15),
        Student('jane', 'B', 12),
        Student('dave', 'B', 10)]""")

student_objects = [
        Student('john', 'A', 15),
        Student('jane', 'B', 12),
        Student('dave', 'B', 10)]

print('\nsorted(student_objects, key=lambda student: student.age)')
print(sorted(student_objects, key=lambda student: student.age))

print("\nOPERATOR MODULE FUNCTIONS")

print("""
The key-function patterns shown above are very common, so Python provides
convenience functions to make accessor functions easier and faster. The operator
module has itemgetter(), attrgetter(), and a methodcaller() function
Using those functions the above examples become simpler.""")

print("""
from operator import itemgetter, attrgetter""")
from operator import itemgetter, attrgetter


print("""
sorted(student_tuples, key=itemgetter(2))""")
print(sorted(student_tuples, key=itemgetter(2)))

print("""
sorted(student_objects, key=attrgetter('age'))""")
print(sorted(student_objects, key=attrgetter('age')))

print("""
Using these accessor makes things easrer and faster. You can also do multiple
levels of sorting using these functions. See documentation.""")






