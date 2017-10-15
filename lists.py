""" Lists """

# most general ver. of a sequence in Py.
# theya are mutable; elements can be changed!


# Assign a list to a variable named my_list

my_list = [1,2,3]

print my_list

print len(my_list)

#Indexing & Slicing

my_list2 = ['one','two', 'three', 4,5]

print my_list2

print my_list2[0] #Grab element at index 0

print my_list2 [1:] #Grab index 1 & everything past it

print my_list2[:3] #Grab everything UP TO index 3

print my_list2 + ['new item'] #concatenate;does NOT change original

# Permanent change to my_list2
my_list2 = my_list2 + ['add new item permanently']
print my_list2

#Make the list double;not permanent
print my_list2*2

"""Basic List Methods"""

l = [1,2,3]
print l

#Append
l.append('append me!')
print l

"""Use pop to 'pop off' an item from the list. By default pop takes off
the last index, but you can also specify which index to pop off."""

# Pop off the 0 idexed item
print l.pop(0)

# Assign the popped element, remember default popped index is -1
popped_item = l.pop()

print popped_item

print l


# We can use the sort method and the reverse methods as well

new_list = ['a', 'e', 'x', 'b', 'c']

print new_list

# use reverse to reverse order (this is PERMANENT!)
new_list.reverse()
print new_list

# use sort to sort the list(alphabetical or numerical/ascending)
new_list.sort()
print new_list

""""Nesting Lists: we can have data structures...
within data structures. For ex: A list inside a list"""

#Lets make three lists
l_1 = [1,2,3]
l_2 = [4,5,6]
l_3 = [7,8,9]

# Make a list of lists to form a matrix
matrix = [l_1, l_2, l_3]
print matrix

"""Now we can again use indexing to grab elements, but know there are
two levels for the index. The items in the matrix object, and then the
items inside that list!"""

# Grab first item in matrix object
print matrix[0]
# Grab first item of the first item in the matrix object
print matrix[0][0]

"""List Comprehensions:
Python has an advanced feature called list comprehensions. They allow
for quick construction of lists. To fully understand this, we need to
understand for loops. So don't worry if you don't completely understand
this section, and feel free to just skip it since we will return to
this topic later."""

#Build a list comprehension by deconstructing a for loop within a []
first_col = [row[0] for row in matrix]
print first_col

# we used list comp. here to grab the first element of every row in the
# matrix object.