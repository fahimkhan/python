#!/usr/bin/python
"""
Serialization (also known as pickling) is a process of converting structured data into data stream format. Through serialization, structures such as lists, tuples, functions, and classes are preserved using ASCII characters between data values. pickling, you can use either module, Pickle or cPickle Both modules function the same, except that the cPickle emodule is written in the C language and is faster and results in better performance
"""

import pickle

class rect:
	def __init__(self,x,y):
		self.l=x
		self.b=y
	def rectarea(self):
		return "Area of rectangle is ",self.l*self.b

r=rect(5,8)
f=open('studentinfo.bin','wb')
pickle.dump(r,f)
f.close()
del r
f=open('studentinfo.bin','rb')
storedobj =pickle.load(f)
print storedobj.rectarea()
