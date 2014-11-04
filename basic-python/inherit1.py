#!/usr/bin/python

#Single level inheritance
# For multiple and multilevel inheritance look book by B.M Harwani
from __future__ import division
class rect:
	def __init__(self):
		self.l = 8
		self.b = 5
	def rectarea(self):
		return self.l*self.b

class triangle(rect):
	def __init__(self):
		rect.__init__(self)
		self.x = 17 
		self.y = 13
	def triangle(self):
		return 1/2*self.x * self.y

r=triangle()
print "Area of rectangle is ",r.rectarea()
print "Area of traingle is ",r.triangle()



