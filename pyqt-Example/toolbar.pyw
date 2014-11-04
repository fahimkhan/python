#!/usr/bin/python 

import sys
from PyQt4 import QtGui


class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        exitaction=QtGui.QAction(QtGui.QIcon('pane.png'),'Exit',self)
        exitaction.setShortcut('Ctrl+Q')
        exitaction.triggered.connect(QtGui.qApp.quit)

        self.toolbar=self.addToolBar('Exit')
        self.toolbar.addAction(exitaction)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Toolbar')    
        self.show()

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
   
    
if __name__ == '__main__':
    main()

