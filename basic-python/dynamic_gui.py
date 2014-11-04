#!/usr/bin/python

from Tkinter import *


## It create list within list dynamically to form gui and get their values return back"

compName='v'
mainlist=['Title:Add Parameter for sine','v1:Initial Voltage','td:Delay Time']


class myframe():
  def __init__(self,parent):
	self.master=parent
	frame=Frame(root)
	print "Hello"
	for item in mainlist:
		word=item.split(':')
		label=Label(frame,text=word[1])
		print "Hi"
		label.grid(sticky=W)
		entry=Entry(frame,width=10)
                entry.grid(sticky=E)
	frame.grid()

root=Tk()
root.title("Additional details")
callframe=myframe(root)
root.mainloop()

		
	
	










