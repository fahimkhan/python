#!/usr/bin/python

import functools

"""
The reduce method returns a single value that is produced by calling the function
on the first two elements of the sequence. The function then is called on the result of
the function and the next element in the sequence, and so on. For example, the
following reduce method computes the sum of the numbers 1 through 10
"""

def add(x,y):
    return x+y	

r=functools.reduce(add,range(1,11))

print "The addition from 1 to 11 is : ",r
