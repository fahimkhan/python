#!/usr/bin/python

##Use of filter method

"""
The filter  method returns a sequence consisting of those elements for which the
included function returns true, those that satisfy the criteria given in the specified
function. If the included function is None , the method returns those elements of the
sequence that are supposed to be returned when the function returns true.
"""

def evenval(x):
    return x%2==0

evens=filter(evenval,range(1,20))
print evens
print (list(evens))	

