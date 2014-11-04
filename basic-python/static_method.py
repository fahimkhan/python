#!/usr/bin/python

"""
A static method is an ordinary function that is built using the staticmethod
decorator and that binds its result to a class attribute. The difference between
static method and a class method is that a static method has no cls sparameter.
It does not use the self parameter, either. There is one more difference-the 
class method is automatically inherited by any child classes, whereas the static method is not. Also, the definition of a static method is immutable via 
inheritance. A static method can be called on a class or on any instance of a 
class.
"""

class rect:
	@staticmethod
	def disp_message():
		l=50
		print "Lenght is",l

rect.disp_message()
r=rect()
r.disp_message()


