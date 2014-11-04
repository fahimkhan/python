from Tkinter import *
 
class AutoScrollbar(Scrollbar):
    # a scrollbar that hides itself if it's not needed.  only
    # works if you use the grid geometry manager.
    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            # grid_remove is currently missing from Tkinter!
            self.tk.call("grid", "remove", self)
        else:
            self.grid()
        Scrollbar.set(self, lo, hi)
    def pack(self, **kw):
        raise TclError, "cannot use pack with this widget"
    def place(self, **kw):
        raise TclError, "cannot use place with this widget"
 
# create scrolled canvas
 
root = Tk()
 
vscrollbar = AutoScrollbar(root)
vscrollbar.grid(row=0, column=1, sticky=N+S)
hscrollbar = AutoScrollbar(root, orient=HORIZONTAL)
hscrollbar.grid(row=1, column=0, sticky=E+W)
 
canvas = Canvas(root,
                yscrollcommand=vscrollbar.set,
                xscrollcommand=hscrollbar.set)
canvas.grid(row=0, column=0, sticky=N+S+E+W)
 
vscrollbar.config(command=canvas.yview)
hscrollbar.config(command=canvas.xview)
 
# make the canvas expandable
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
 
# create canvas contents
 
frame = Frame(canvas)
frame.rowconfigure(1, weight=1)
frame.columnconfigure(1, weight=1)
 
# Label for name
Label1 = Label( frame, width = 40, height = 2, text = 'haiyan', font = "Arial 20" )
Label1.grid( row = 0, rowspan = 1, column = 1, columnspan =6, sticky = W+E+N+S )
 
rows = 100
cols = 10
# Create one button object and one variable for all the buttons
Button_Name = [[Checkbutton() for i in range(rows)] for j in range(cols)]
buttonChecked = [[BooleanVar() for i in range(rows)] for j in range(cols)]
buttonNameVar = [[StringVar() for i in range(rows)] for j in range(cols)]
 
for boat_num in xrange(cols):
   for boat_slot in xrange(rows):
 
      # Freeze the column number to toggle whole column on or off
      def handler_col(i=boat_num):
         return select_full_column(i)
 
      # Freeze the row number to toggle whole row on or off
      def handler_row(i=boat_slot):
         return select_full_row(i)
 
      # For button Button_Name[0][0] to control all boats/slots
      if boat_slot == 0 and boat_num == 0:
         Button_Name[boat_num][boat_slot] = Checkbutton(frame,
                                                            text = 'All Boats_Slots',
                                                            padx=5, pady=5,
                                                            relief = SUNKEN,
                                                            width = 15,
                                                            bg = 'Moccasin',
                                                            variable = buttonChecked[boat_num][boat_slot],)
##                                                            command = select_all_boats)
 
      # For button Button_Name[i][0], i is range(1,boat_num+1) to control all slots in boat i
      elif boat_slot == 0:
         Button_Name[boat_num][boat_slot] = Checkbutton(frame,
                                                            text = 'Boat_' + str(boat_num),
                                                            padx=5, pady=5,
                                                            relief = SUNKEN,
                                                            width = 15,
                                                            bg = 'light yellow',
                                                            variable = buttonChecked[boat_num][boat_slot],)
##                                                            command = handler_col)
 
      # For button Button_Name[0][i], i is range(1,boat_slot+1) to control all slots in row i
      elif boat_num == 0:
         Button_Name[boat_num][boat_slot] = Checkbutton(frame,
                                                            text = 'Slot_' + str(boat_slot),
                                                            padx=5, pady=5,
                                                            relief = SUNKEN,
                                                            width = 15,
                                                            bg = 'light yellow',
                                                            variable = buttonChecked[boat_num][boat_slot],)
##                                                            command = handler_row)
 
      # For single button control
      else:
         Button_Name[boat_num][boat_slot] = Checkbutton(frame,
                                                            textvariable = buttonNameVar[boat_num][boat_slot],
                                                            padx=5, pady=5,
                                                            relief = SUNKEN,
                                                            variable = buttonChecked[boat_num][boat_slot],
                                                            width = 15,)
##                                                            command = select_current_slot)
 
      # Lay out check buttons with grid manager
      Button_Name[boat_num][boat_slot].grid(row = boat_slot+1, rowspan = 1, column = boat_num + 2, columnspan = 1)
 
 
canvas.create_window(0, 0, anchor=NW, window=frame)
 
frame.update_idletasks()
 
canvas.config(scrollregion=canvas.bbox("all"))
 
root.mainloop()
