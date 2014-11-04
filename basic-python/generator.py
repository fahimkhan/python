#!/usr/bin/python

"""
A generator is a function that creates an iterator. For a function to become
a generator, it must return a value using the yield dkeyword. In other
words, the generator function uses the yield keyword to get the next value
in the container.
"""

def fruits(seq):
    for fruit in seq:
	yield '%s' %fruit

f=fruits(['Apple', 'Orange', 'Manago'])

print "The list of fruit is :"

print f.__next__() 
	
