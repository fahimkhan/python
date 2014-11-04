#!/usr/bin/python

from Tkinter import *

class WinDos:

    def __init__(self,mainWin):
        self.mainWin = mainWin


        Label(self.mainWin, text="Main Window").pack()
        b1 = Button(self.mainWin, text="switch to win 2!", command=self.win2up)
        b1.pack()




        self.secondWin = Toplevel()
        Label(self.secondWin, text="SecondWin").pack()
        b2 = Button(self.secondWin, text="Switch to first window!", command=self.win1up)
        b2.pack()
        self.secondWin.withdraw()  # Hide this window until we need it!

    def win1up(self):
        print("Switching to window 1!")
        self.secondWin.withdraw()
        self.mainWin.deiconify()

    def win2up(self):
        print("Switching to window 2!")
        self.mainWin.withdraw()
        self.secondWin.deiconify()



mw = Tk()
myApp = WinDos(mw)
mw.mainloop()
