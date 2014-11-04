#!/usr/bin/python
 
"""
Poly means many, and morph means change. Through polymorphism, you
can have a method with the same name in different classes to perform
different tasks. You can handle objects of different types in the same way.
To implement polymorphism, you define a number of classes or subclasses
that have method(s) with the same name. These classes or subclasses are
polymorphic. You can access the polymorphic methods without knowing
which class or subclass is invoked.
For example, the commission percentage from selling a book may be
different for a stockist, a distributor, and a retailer. You can define a
commision method in three classes-stockist,distributor,retailer 
where each method computes a different percentage of dealer commission. On execution of the program, the respective commsision
method is called on each instance. Here is a complete program that
demonstrates polymorphism.
"""

class book:
	def __init__(self,x):
		self.price=x

class stocklist(book):
	def __init__(self,x):
		book.__init__(self,x)
	def commission(self):
		self.comm=self.price*5/100
		print "Commission of stockiest is %.2f" %self.comm
class distributor(book):
	def __init__(self,x):
		book.__init__(self,x)
	def commission(self):
		self.comm=self.price*8/100
		print "Commission of distributor is %.2f " %self.comm

class retailer(book):
	def __init__(self,x):
		book.__init__(self,x)
	def commission(self):
		self.comm=self.price*10/100
		print "Commission of retailer is %.2f "  %self.comm

r=stocklist(100)
s=distributor(100)
t=retailer(100)

prncomm=[r,s,t]
for c in prncomm:
	c.commission()


