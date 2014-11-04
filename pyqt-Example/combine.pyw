#!/usr/bin/python 

import sys
from PyQt4 import QtGui

class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        textEdit=QtGui.QTextEdit()
        self.setCentralWidget(textEdit)

        exitaction=QtGui.QAction(QtGui.QIcon('pane.png'),'Exit',self)
        exitaction.setShortcut('Ctrl+Q')
        exitaction.setStatusTip('Exit Application')
        exitaction.triggered.connect(self.close)

        self.statusBar().showMessage('statusBar')

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitaction)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitaction)
        
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')    
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    
