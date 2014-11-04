#!/usr/bin/python

class book:
	price=100
	@classmethod
	def display(cls):
		print (cls.price)

	def show(self,x):
		self.price = x
		print (self.price)

b=book()
c=book()

book.display()
b.display()
c.show(200)
b.show(300)




