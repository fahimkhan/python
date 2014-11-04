#!/usr/bin/python

from Tkinter import *
import fileinput
import tkMessageBox
import os
class AutoScrollbar(Scrollbar):
    # a scrollbar that hides itself if it's not needed.  only
    # works if you use the grid geometry manager.
    def set(self,lo,hi):
     #   if float(lo) <= 0.0 and float(hi) >= 1.0:
      #      # grid_remove is currently missing from Tkinter!
       #     self.tk.call("grid", "remove", self)
        #else:
         #   self.grid()
        Scrollbar.set(self,lo,hi)
""" def pack(self, **kw):
        raise TclError, "cannot use pack with this widget"
    def place(self, **kw):
        raise TclError, "cannot use place with this widget"
        """


class myframe():
	def __init__(self,parent):
		self.master=parent
		#Creating MenuBar
		menubar=Menu(parent)
		filemenu=Menu(menubar,tearoff=0)
		filemenu.add_command(label="Save", command=self.file_save)
		filemenu.add_command(label="Exit",command=self.exit_window)
		menubar.add_cascade(label="File", menu=filemenu)
		#Display menu
		parent.config(menu=menubar)
		
		#Creatin Canvas Object
		vscrollbar = AutoScrollbar(parent)
		vscrollbar.grid(row=0, column=1, sticky=N+S)
		hscrollbar = AutoScrollbar(root, orient=HORIZONTAL)
		hscrollbar.grid(row=1, column=0, sticky=E+W)
		c_obj=Canvas(parent,height=400,width=400,yscrollcommand=vscrollbar.set,xscrollcommand=hscrollbar.set)
		c_obj.grid(row=0, column=0, sticky=N+S+E+W)
		vscrollbar.config(command=c_obj.yview)
		hscrollbar.config(command=c_obj.xview)
		
		# make the canvas expandable
		root.grid_rowconfigure(0, weight=1)
		root.grid_columnconfigure(0, weight=1)
		
		# create canvas contents
		frame = Frame(c_obj)
		frame.rowconfigure(1, weight=1)
		frame.columnconfigure(1, weight=1)
		
		frame1=Frame(parent)
		label0= Label(frame1,text='Note:',font="Arial 20")
		label0.grid(sticky=W)
		
		#Iterating note file for user
		for line in fileinput.input(['note.txt']):
			label1=Label(frame1,text=line,pady=0,padx=0,width=0)
			label1.grid(sticky=W)
		frame1.grid()
		global var
		var={}
		global count
		count=0
		
		##Checking for exitance of file 
		fname="comp_value.txt"
		if os.path.exists(fname):
			print "File found"
			for line in fileinput.input(['comp_value.txt']):
				column=line.split(':')
				label=Label(frame,text=column[0])
				label.grid(row=count,sticky=W+E+N+S)
				var[count] = StringVar()
				entry=Entry(frame,width=10,textvariable=var[count])
				entry.grid(row=count,column=1,sticky=W+E+N+S,padx=0,pady=0)
				var[count].set(column[1].strip())
				count=count+1
				
		else:
			print "File Not Found"		
			for line in fileinput.input(['comp_list.txt']):
				label=Label(frame,text=line)
				label.grid(row=count,sticky=W+E+N+S)
				var[count] = StringVar()
				entry=Entry(frame,width=10,textvariable=var[count])
				entry.grid(row=count,column=1,sticky=W+E+N+S,padx=0,pady=0 )
				count=count+1
		c_obj.create_window(0, 0, anchor=NW, window=frame)
		frame.update_idletasks()
		c_obj.config(scrollregion=c_obj.bbox("all"))
			

	def file_save(self):
		global count
		global var
		print "Total Number of Elements : "+str(count)
		count = 0
		infile = open("comp_list.txt", 'r') # open file for reading
		outfile = open("comp_value.txt",'w') # open file for writing
		
		for line in infile.readlines():
			print line.strip()+':'+var[count].get().strip()
			outfile.write(line.strip()+':'+var[count].get().strip())
			outfile.write("\n")
			count+=1
		infile.close()
		outfile.close()
		
	def exit_window(self):
		self.master.quit()	
	
		
##Program Starts from here		
root = Tk()
root.title("Component Detail")
#Message Dialouge Box
tkMessageBox.showinfo("Enter Value","Please Enter the value of component" )
hello = myframe(root)
root.mainloop()


