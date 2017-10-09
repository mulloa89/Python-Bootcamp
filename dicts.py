"""Dictionaries"""
# print dict --> prints full dictionary
# print dict['key1'] --> prints 1st key's value

dict1 = {'key1':'value','key2':'value'}
print dict1
print dict1['key1']

dict2 = {'key1': 123, 'key2':3.4,'key3':'string'}
print dict2
print dict2['key1']

#Creating a dictionary
d = {}
d['k1'] = 1
d['k2'] = 2
d['k3'] = 3
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
print d.keys()  #returns list of all keys
print d.values()    #grabs all values
print d.items() #returns tuples of all items