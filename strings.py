"""Strings"""

"""Used in python to record text info; name. Viewed as a sequence by
Py. Can be indexed to grab particular letters."""

# We can print strings in single & double quotes

print 'Hi there!'
print "Sup dawg!"

"""Be carefull with quotes within strings"""

# printing the following will result in a error
# print 'I'm using single quotes, but will create an error.
# fixed
print "Now I'm ready to use single quotes inside strings!"

# Use \n to print a new line
print "Hello World! \nHello there, again!"

# len() outputs the length of a string
print len('Hello World')

"""Indexing"""

s = 'Hello World'

# Show first element (in this case a letter)
print s[0]
print s[1] #shows 2nd element

# We can use a : to perform Slicing!
# Slicing grabs everything up to a designated point

print s[1:] # grab everything past first term 'til the end of string.
# Slicing does NOT change the original variable.

print s[:3] # grab everything UP TO 3rd index

print s[:] # Everything!

# We can also use negative indexing to go backwards

print s[-1] # Last letter (one index behind 0 so it loops back around)

print s[:-1] # Grab everything but the last letter

""" We can also use index and slice notation to grab elements of a
sequence by a specified step size (default is 1). For instance we can
use two colons in a row and then a number specifying the frequency to
grab elements."""

# Grab everything, but in step size of 1
print s[::1]

# Grab everything, but in step sizes of 2
print s[::2]

# Prints string backwards
print s[::-1]

""" String Properties: strings have an important property known as
immutability. This means that once a string is created, the elements
within it can not be changed or replaced. For example: """

# s[0] = x !! will return error/ item assignment not suported


# Concatenate strings! (...to link together)

print s + ' concatenate me!'

# We can reassign 's' completely
s = s + ' concatenate me!'
print s

# We can use the multiplication symbol to create repitition!
letter = 'z'
print letter*10

""" Basic Built-in String Methods"""

print s

print s.upper() #Upper case a string
print s.lower() #lower case a string
print s.split() # Split a string by blank space (default)
print s.split('W') #Split by a specific element(element not included)

"""Print Formatting: We can use the .format() method to add formatted
objects to printed string statements."""

print 'Insert another string with curly brackets: {}'.format('The inserted string.')