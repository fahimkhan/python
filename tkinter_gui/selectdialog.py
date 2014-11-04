#!/usr/bin/python
import Tkinter
import Pmw

class Demo():
    def __init__(self, parent):
	# Create the dialog.
	self.dialog = Pmw.SelectionDialog(parent,
	    title = 'selectiondialog',
	    buttons = ('OK', 'Cancel'),
	    defaultbutton = 'OK',
	    scrolledlist_labelpos = 'n',
	    label_text = 'Which place do u like?',
	    scrolledlist_items = ('kansas','Chicago','florida','california','newyork',
		'washington D.C','sanfrancisco', 'virginia', 'new jersey', 'boston',
		'maryland'),
		command = self.execute,
	)
	self.dialog.withdraw()
	self.dialog.pack(fill = 'both', expand=1, padx=5, pady=5)
	self.dialog.deactivate()

	# Create button to launch the dialog.
	w = Tkinter.Button(parent, text = 'Show selection dialog',
	        command = self.dialog.activate)
	w.pack(padx = 8, pady = 8)

    def execute(self, result):
	sels = self.dialog.getcurselection()
	if len(sels) == 0:
	    print 'You clicked on', result, '(no selection)'
	

	else:
	    print 'You clicked on\n', result, sels[0]
	self.dialog.deactivate(result)

# Create demo in root window for testing.
if __name__ == '__main__':
    root = Tkinter.Tk()
    Pmw.initialise(root)
    root.title("Select Dialog")
    exitButton = Tkinter.Button(root, text = 'Exit', command =
root.destroy)                                               
    exitButton.pack(side = 'bottom')
    widget = Demo(root)
    root.mainloop()


