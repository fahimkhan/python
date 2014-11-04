#!/usr/bin/python

from Tkinter import *
import fileinput
root=Tk()
canvas=Canvas(root,bg='#FFFFFF',width=300,height=300,scrollregion=(0,0,500,500))
win_obj=canvas.create_window(0,0,anchor='center',state='normal')

frame=LabelFrame(canvas,width=300,height=300)
frame.grid(row=0,column=0)

#canvas=Canvas(frame,bg='#FFFFFF',width=300,height=300,scrollregion=(0,0,500,500),xscrollincrement=0)
hbar=Scrollbar(frame,orient=HORIZONTAL)
#hbar.pack(side=BOTTOM,fill=X)
hbar.grid()
hbar.config(command=canvas.xview)
vbar=Scrollbar(frame,orient=VERTICAL)
#vbar.pack(side=RIGHT,fill=Y)
vbar.grid()
vbar.config(command=canvas.yview)
for line in fileinput.input(['comp_value.txt']): 
	left = Label(frame, text=line)
	left.grid()
	entry = Entry(frame,width=10)
	entry.grid()
canvas.config(width=300,height=300)
canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
canvas.grid()

root.mainloop()

#def makeentry(self,parent, caption, width=None, **options):
	#	Label(parent, text=caption).pack(side=LEFT)
	#	entry = Entry(parent, **options)
	#	if width:
	#		entry.config(width=width)
	#	entry.pack(side=LEFT)
	#	return entry

	#user = makeentry(parent, "User name:", 10)
	#password = makeentry(parent, "Password:", 10, show="*")
