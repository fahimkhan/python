#!/usr/bin/python
from Tkinter import *

class Page(Frame):
    def __init__(self, root, id):
        Frame.__init__(self, root)
        pages = ["This is the info on page 0",
                 "This is the info on page 1",
                 "This is the info on page 2",
                 "This is the info on page 3",
                 "This is the info on page 4"]
        Label(self, text=pages[id]).pack(fill=BOTH)

class Application(Frame):
    """Main application where everything is done"""
    def __init__(self, root):
        Frame.__init__(self, root)
        self.root = root
        self.page = 0
        self.pages = [Page(self, x) for x in range(5)]#creates list of 5 pages
        self.pages[self.page].grid(row=0, column=0, columnspan=2)
        Button(self, text="Next", command=self.next).grid(row=1, column=1)
        Button(self, text="Back", command=self.back).grid(row=1, column=0)

    def next(self):
        """changes the current page. I've only done next here, but you could
        do backwards, skip pages, etc"""
        self.pages[self.page].grid_forget() #remove the current page
        self.page += 1
        if self.page >= 5: #checking haven't gone past the end of self.page
            self.page = 4
        self.pages[self.page].grid(row=0, column=0, columnspan=2)
        
    def back(self):
        self.pages[self.page].grid_forget()
        self.page -= 1
        if self.page < 0:
            self.page = 0
        self.pages[self.page].grid(row=0, column=0, columnspan=2)
        
if __name__ == "__main__":
    root = Tk()
    app = Application(root)
    app.pack()
    root.mainloop()


