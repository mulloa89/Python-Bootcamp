"""Dictionaries(hash tables)"""

""" Mappings are a collection of objects that are stored by a key, unlike
a sequence that stored objects by their relative position. This is an
important distinction, since mappings won't retain order since they
have objects defined by a key. """

""" A python dictionary consists of a key and then an associated value. 
That value can be almost any python object. """


# print dict --> prints full dictionary
# print dict['key1'] --> prints 1st key's value

dict1 = {'key1':'value','key2':'value'}
print dict1
print dict1['key1']

#It's important to note that dictionaries are very flexible in the data
#types they can hold

dict2 = {'key1': 123, 'key2':3.4,'key3':'string'}
print dict2
#lets call items from the dictionary
print dict2['key1']
# Can call an index on that value
print dict2['key3'][0]
#Can even call methods on that value
print dict2['key3'][0].upper()

#We can effect the values of a key as well...
print dict2['key1']
#subtract 123 from the value
dict2['key1'] = dict2['key1'] - 123
#check it...
print dict2['key1']

""" Python has a built-in method of doing a self subtraction or
addition (or multiplication...division). we could have also
used += or -= for the above statement. for example..."""

#set the object equal to itself minus 123
dict2['key1'] -= 123
print dict2

"""We can also create keys by assignment.for instance if we started off
with an empty dictionary, we could continually add to it."""

#Creating a dictionary
d = {}
#create a new key through assignment
d['animal'] = 'Dog'
d['answer'] = 42
print d

#Nesting with Dictionaries

#Dictionary nested inside a dictionary nested inside a dictionary
k = {'key1':{'nestkey':{'subnestkey':'value'}}}
print k

#print until we only print 'value'
print k['key1']
print k['key1']['nestkey']
print k['key1']['nestkey']['subnestkey']

#Dictionary methods

q = {'key1':1,'key2':2,'key3':3}
print q.keys()  #returns list of all keys
print q.values()    #grabs all values
print q.items() #returns tuples of all items