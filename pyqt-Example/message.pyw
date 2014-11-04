#!/usr/bin/python

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
	def __init__(self):
		super(Example,self).__init__()
		self.initUI()
	def initUI(self):
		self.setGeometry(400,400,400,400)
		self.setWindowTitle("Message")
		self.show()
	def closeEvent(self,event):
		reply=QtGui.QMessageBox.question(self,'Message',"Are you sure to quit?",QtGui.QMessageBox.Yes|QtGui.QMessageBox.No, QtGui.QMessageBox.No)

		if reply==QtGui.QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    show()

def show():
    print "Its Working"

if __name__ == '__main__':
    main()	
		






		
