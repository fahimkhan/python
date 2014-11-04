#!/usr/bin/python

""" The iter method is used to get an iterator object. The iter(object)
method calls that object's __iter__ method to get an iterator object. Once,
you get an iterator object, you can iterate over the object using its next()
method.

"""

names=['Jack','Joshep','Ram','Rahim','Virat']

itr = iter(names)
print itr
print (itr.__next__())
print (itr.__next__())
print (itr.__next__())
print (itr.__next__())
print (itr.__next__())
print (itr.__next__())	

