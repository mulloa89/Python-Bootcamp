# Assign a lsit to a variable named my_list

my_list = [1,2,3]

print my_list

print len(my_list)

my_list2 = ['one','two', 'three', 4,5]

print my_list2

print my_list2[0]

print my_list2 [1:]

print my_list2[:3]

print my_list2 + ['new item']

new_list = ['a', 'e', 'x', 'b', 'c']

print new_list

l_1 = [1,2,3]
l_2 = [4,5,6]
l_3 = [7,8,9]

matrix = [l_1, l_2, l_3]
print matrix
print matrix[0]
print matrix[2][0]

first_col = [row[0] for row in matrix]
print first_col