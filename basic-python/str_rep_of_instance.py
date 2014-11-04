#!/usr/bin/python

class rect:
	def __init__(self,x,y):
		self.l=x
		self.b=y
	def __str__(self):
		return 'lenght is %d, Breadth is %f' %(self.l,self.b)
	def area(self):
		return self.l*self.b

r=rect(5,8)
print (r)
print "Area of rectangle is ",r.area()

