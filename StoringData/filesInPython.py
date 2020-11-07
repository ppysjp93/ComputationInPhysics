print("##################################################") 
print("""
FILES IN PYTHON""")
print("##################################################") 
 

print("""
In python to open a file there is the open() function
the following programme reads the each line from the matrix.txt file""")

print("\nEXAMPLE 1")

f = open('matrix_0.txt')
matrix = []
for line in f.readlines():
    row = [int(x) for x in line .split(',')]
    print("\nrow = \n", str(row))
    matrix.append(row)
f.close

print(matrix)

print("""
The lines from a file are always a string in python so be aware of this. This
means that you have to tell python how exactly to interpret the file and convert
each value to whatever seems fit.
There are also flags which can be added to reading in a file which will set how
the data can be manipulated, the flags are 'r', 'w', 'a' and '+'.""")

print("\nEXAMPLE 2")
print("""
In this next example we are going to open the matrix file with 'r+' flag which
means that we are going to be able to change the file from within this script.
\n = open('matrix.txt', 'r+') Open the files in read and write mode
\norig = f.read() Reads the entire file into a string.
\nf.seek(0) Goes back to the start of the file.
\nf.write('0,0,0,0') White a new line clobbering what was there.
\nf.write(orig) Write the original contets back to the file after the line
that was just added.
\nf.write('1,1,1,1') Writes another new line after the original contents.
\nf.close() Closes the file now that we are done with it.""")

f = open('matrix_0.txt', 'r+')
orig0 = f.read() 
print("\norig0 = \n", str(orig0))

f = open('matrix.txt', 'r+')
orig1 = f.read() 
f.seek(0) 
f.write('0,0,0,0\n') 
f.write(orig1)
f.write('\n1,1,1,1') 
f.close()
print("\norig1 = \n", str(orig1))

