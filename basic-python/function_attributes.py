#!/usr/bin/python

""" Example of any function attributes """

def sum(a,b=5):
   "Add the two numbers"
   return a+b

sum.version="1.0"
sum.author="fahim"
k=sum(10,20)

print "The sum is ",k
print "The documentation string is ",sum.__doc__
print "The default function values are ",sum.__defaults__
print "The function name is " ,sum.__name__
print "The code object of function is ",sum.__code__
print "The dictionary of function is ",sum.__dict__		

