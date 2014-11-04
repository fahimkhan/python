#!/usr/bin/python

class rect:
        def __init__(self,x,y):
                self.__l=x
                self.__b=y
        def rectarea(self):
                return self.__l * self.__b

r=rect(5,8)
print "Area of rect is ",r.rectarea()
print "Area of rect is ",r._rect__l*r._rect__b

