#!/usr/bin/python

class product:
      count=0
      def __init__(self,name):
	self.name=name
	product.count += 1
      @staticmethod
      def prodstatcount():
	return product.count
      @classmethod
      def prodclasscount(cls):
	print 'Class info:',cls
	print 'Class method -The product count is :',cls.count

p1=product('Camera')
p2=product('Cell')
print "Static Method-The product count is:",product.prodstatcount()
p2.prodclasscount()
		
