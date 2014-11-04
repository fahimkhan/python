#!/usr/bin/python 

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        okbutton=QtGui.QPushButton("OK")
        cancelbutton=QtGui.QPushButton("Cancel")

        hbox=QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okbutton)
        hbox.addWidget(cancelbutton)
        
        vbox=QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)
        self.setGeometry(300,300,200,200)
        self.setWindowTitle("Button")
        self.show()

def main():
    app=QtGui.QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()


            
