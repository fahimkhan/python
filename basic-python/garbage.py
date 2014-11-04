#!/usr/bin/python

class rect:
	n=0
	def __init__(self,x,y):
		rect.n += 1
		self.l=x
		self.b=y

	def __del__(self):
		rect.n -= 1
		class_name = self.__class__.__name__
		print(class_name,' destroyed')
	def rectarea(self):
		print "Area of rectangle is : ",self.l*self.b

	def noOfObject(self):
		print "Number of objects are :",rect.n

r=rect(3,5)
r.rectarea()
s=rect(5,8)
s.rectarea()
r.noOfObject()

del r
s.noOfObject()
del s

  	
