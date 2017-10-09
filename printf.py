"""Print Formatting"""

print 'This is a string ' #most basic example of a print statement

# you can use the %s to format strings into your print statements
s = 'STRING'
print 'Place another string with a mod and s: %s' %(s)

"""Floating Point Numbers:
Floating point numbers use the format %n1.n2f where the n1 is the total
minimum number of digits the string should contain (these may be filled
with whitespace if the entire number does not hve this many digits.)
The n2 placeholder stands for how many numbers to show past the
decimal point. Lets see some examples:"""

print 'Floating point numbers: %1.2f' %(13.144)

print 'Floating point numbers: %1.0f' %(13.144)

print 'Floating point numbers: %1.5f' %(13.144)

print 'Floating point numbers: %10.2f' %(13.144)

print 'Floating point numbers: %25.2f' %(13.144)


"""Conversion Format methods.
It should be noted that two methods %s and %r actually convert any
python object to a string using two separate methods: str() and repr().
We will learn more about these functions later on in the course, but
you should note you can actually pass almost any Python object with
these two methods and it will work:"""

print 'Here is a number: %s. Here is a string: %s' %(123.1,'hi')

print 'Here is a number: %r. Here is a string: %r' %(123.1,'hi')

""" Multiple Formatting: Pass a tuple to the modulo symbol to place
multiple formats in your print statements:"""

print 'First: %s, Second: %1.2f, Third: %r' %('hi',3.14,22)

"""Using the string.format() method: the best way to format objects
into your strings for print statements is using the format method.
The syntax is:
    
    'String here {var1} then also {var2}'.format(var1='something1
    ',var2='something2')

Lets see some examples:    """

print 'This is a string with an {p}'.format(p='insert')

#Multiple times:
print 'One: {p}, Two: {p}, Three: {p}'.format(p='Hi!')

#Several Objects
print 'Object 1: {a}, Object 2: {b}, Object 3: {c}'.format(a=1,b='two',c=12.3)
