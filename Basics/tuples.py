""" Tuples: lists that cannot be changed. They are used to present
things that shouldn't be changed, such as days of the week, or dates
on a calendar."""

# Constructing Tuples: use () w/elements separated by commas

t = (1,2,3)
print len(t)

# Can also mix object types

t = ('one',2)

# Use indexing just like we did in lists
print t[0]

# Slicing just like a list
print t[-1]


"""Basic Tuple Methods"""

# Use .index to enter a value and return the index
print t.index('one')

# Use .count to count the # of times a value appears
print t.count('one')

"""Immutability: THEY CANNOT BE CHANGED!"""
# they cannot grow; can't be added to

"""When to use tuples:
They are used when immutability is necessary. it provided a convenient
source of data integrity."""