#!/usr/bin/python

import sys
from PyQt4 import QtGui

class app_icon(QtGui.QWidget):
	def __init__(self):
		super(app_icon, self).__init__()
		self.initUI()

	def initUI(self):
		self.setGeometry(300,300,200,150)
		self.setWindowTitle("App-Icon")
		self.setWindowIcon(QtGui.QIcon('pane.png'))
		self.show()


def main():
	
	app = QtGui.QApplication(sys.argv)
    	ex = app_icon()
    	sys.exit(app.exec_())


if __name__ == '__main__':
    main()    
