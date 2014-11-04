#!/usr/bin/python

matter=''' Python is great language.
	It is very easy to lear and can be used as oop and web
	devlopement also'''

f=open('aboutbook.txt','w')
f.write(matter)
f.close()
f=open('aboutbook.txt')

while True:
	line=f.readline()
	if len(line)==0:
		break
	print line

f.close()

### Few file object method
"""
fileno() - Returns the internal file descriptor used by the OS
	   library when working with this file.

isatty() - Returns true if the file is connected to the console
	   or keyboard.

closed  - This attribute is true if the file is closed.

mode   -  This attribute is the mode of the file that was used
	  to create the file object through the open() function.

name   -  This attribute is the filename that was passed to
	  the open() function when creating the file object.
"""



 	

