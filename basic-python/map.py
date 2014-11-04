#!/usr/bin/python

"""
The map method calls the included function for each of the elements in the sequence
and returns a list of the returned values.
"""

def square(x):
    return x*x

sqr=map(square,range(1,11))

print (list(sqr))
print sqr
