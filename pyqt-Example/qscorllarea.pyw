#!/usr/bin/python 

import sys
from PyQt4.QtGui import *
from random import choice

class ThisWindow(QtGui.QWidget):
    def __init__(self,parent=None):
        super(ThisWindow,self).__init__()
        l=QVBoxLayout(self)

        l.setContentsMargins(0,0,0,0)
        l.setSpacing(0)
       
        s=QScrollArea()
        l.addWidget(s)    
        w=QWidget(self)
        vbox=QVBoxLayout(w)
        for x in range(0, choice(range(50,150))):
            _l=QHBoxLayout()
            _l.addWidget(QLabel("Label # %d" % x, self))
            _l.addWidget(QCheckBox(self))
            _l.addWidget(QComboBox(self))
            _l.addStretch(1)
            vbox.addLayout(_l)
                                                                                  
        s.setWidget(w)
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("This is how you make the window scroll if it gets beyond a certain height")
       
    
if __name__=="__main__":
    from sys import argv, exit
    a=QApplication(argv)
    win=ThisWidget()
    win.show()
    win.raise_()
    exit(a.exec_())

