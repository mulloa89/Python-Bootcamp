""" Sec.3 - Objects & Data Structures Assessment Test"""

"""

**TEST YOUR KNOWLEDGE**

Write a brief description of all the following Object Types &
Data Structures we've learned about:

Numbers: Integers(1,2,3) or floating points (1.2, 2.0, 3.5); can do
basic math in py; + - / *; follow order of operations; x*2 - exponent;
x**0.5 - square root

Strings: print "hello world"; print 'hello world'; can be concactenated
or added too; can be reassigned;

Lists: mutable - can be changed; assigned to a variable

Tuples: lists that cannot be changed;

Dictionaries: immutable; values assigned to a key; no order

"""



""" **NUMBERS** """

# Write an equation that uses mult, division, an exponent, addition, & 
# subtraction that is equal to 100.25

y = 200 / 2 * 1**1 + 0.50 - 0.25
print y


# Q1 --> 44
a = 4 * (6+5)
print a
# Q2 --> 29
b = 4 * 6 + 5
print b
# Q3 --> 34: 6*5, +4=34
c = 4 + 6 * 5
print c

""" Strings """
s = 'hello'

# print out 'e' using indexing
print s[1]

# reverse the string using indexing
print s[::-1]

# give two methods of producing 'o' using indexing
print s[4]
print s[-1]

""" Lists """

# Build this list [0,0,0] two separate ways

list_1 = [0,0,0]
print list_1

list_2 = []
print list_2

list_2 = [] + [0,0,0]
print list_2

list_3 = [0]
print list_3*3

# reassign 'hello' in this nested list to say 'goodbye' item in list:
l = [1,2,[3,4,'hello']]
print l

l[2] = [3,4,'goodbye'] # or -- l[2][2] = 'goodbye'
print l

# sort the list below
l = [5,3,4,6,1]
print l
l.sort() # or -- sorted(l) > print l
print l

"""Dictionaries"""

# Using keys and indexing, grab 'hello' from the following dictionaries

d = {'simple_key': 'hello'}
print d['simple_key']

d = {'k1':{'k2':'hello'}}
print d['k1']['k2']

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print d['k1'][0]['nest_key'][1][0]

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print d['k1'][2]['k2'][1]['tough'][2][0]

# Can you sort a dictionary? Why or why not?
# answer: dicts cannot be sorted; the dont have orders; just keys
# answer from prof: no! normal dicts are mappings, not a sequence

"""Tuples"""

# major difference between tuples and lists?
# answer: tuples are immutable(cant change) & lists are mutable

# how to created a tuple
t = (1,2,3)
print t

"""Sets"""
# what is unique about a set?
# answer: the don't allow for duplicate items.

# use a set to find the uniqe values of the list below:

l = [1,2,2,33,4,4,11,22,3,3,2]

set(l) # use set function
print l

"""Booleans"""

# 2 > 3 = False
# 3 <= 2 = False
# 3 == 2.0 = False
# 3.0 == 3 = True
# 4**0.5 != 2 = False

""" Final question: What is the boolean ouput of the following: """

# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False
l_one [2][0] >= l_two[2]['k1']

# Answer: 3 >= 4 --> False


