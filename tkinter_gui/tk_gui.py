#!/usr/bin/python

from Tkinter import *
import math
import tkMessageBox


root=Tk()
top=Frame(root)
top.pack(side='top')


hwtext = Label(top, text='Hello, World! The sine of')
hwtext.pack(side='left')

r=StringVar()
r.set('1.2')
r_entry=Entry(top,width=6,textvariable=r)
r_entry.pack(side='left')
s = StringVar() # variable to be attached to s_label

def comp_s():
	
	global s
	s.set('%g' % math.sin(float(r.get()))) # construct string
def quit(event):
	if tkMessageBox.askokcancel('Quit','Do you really want to quit?'):
		root.destroy()	
compute = Button(top, text='equals', command=comp_s)
compute.pack(side='left')
s_label = Label(top, textvariable=s, width=18)
s_label.pack(side='left')
root.bind('<q>',quit)
root.mainloop()

