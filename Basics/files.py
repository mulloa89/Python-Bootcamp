"""Files:**will probably need to install certain libraries or modules
to interact with various file types. Python has a built-in open
function to open and play with basic file types."""

# Open the test.txt we made earlier
my_file = open('test.txt')
# We can now read the file
my_file.read()

# But what happens if we try to read it again?
my_file.read()

# ^^result of line 11 because reading "cursor" is at the end of the file.

#Seek to the start of file (index 0)
my_file.seek(0)
#now read again
my_file.read()

# To automatically reset cursor, use readlines method
# caustion w/ large files; all held in memory
my_file.readlines()

"""Writing to a File"""

# Add a second argument to the function, 'w' - write
my_file = open('test.txt','w+')
# Write to the file
my_file.write('This is a new line.')
# Read the file
my_file.read()

