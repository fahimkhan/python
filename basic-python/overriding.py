#!/usr/bin/python

"""
If in a derived class you have a member function with the same signature
as that of the base class, then you say that the member function of the
derived class is overriding the member function of the base class. If the
member function is invoked by the instance of the derived class, the
member function of the derived class will be executed (and not the
member function of the base class).
"""

from __future__ import division

class rect:
	def __init__(self):
		self.l=8
		self.b=5
	def area(self):
		return self.l*self.b

class triangle(rect):
	def __init__(self):
		rect.__init__(self)
		self.x = 17
		self.y = 13
	def area(self):
		return 1/2*self.x*self.y

r=triangle()
print "Area of triangle is ",r.area()

