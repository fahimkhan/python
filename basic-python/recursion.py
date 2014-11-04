#!/usr/bin/python

def addseq(x):
   if x==1:
	return 1
   else:
	return x + addseq(x-1)

def factorial(x):
    if x==1:
	return 1
    else:
	return x*factorial(x-1)	

print "The sum of first 10 seq is : ",addseq(10)		
print "The factorial of a number is :",factorial(10)
