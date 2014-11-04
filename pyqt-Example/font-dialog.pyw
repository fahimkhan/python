#!/usr/bin/python 

#The QtGui.QFontDialog is a dialog widget for selecting a font. 

from PyQt4 import QtGui,QtCore
import sys

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example,self)
        self.initUI()

    def initUI(self):
        vbox=QtGui.QVBoxLayout()
        self.btn=QtGui.QPushButton('Dia',self)
        self.btn.setSizePolicy(QtGui.QSizePolicy.Fixed)

        self.btn.move(20,20)
        vbox.addWidget(btn)

        self.btn.cliked.connect(self.showDialog)
        self.lbl=QtGui.QLabel("Knowledge Matters",self)
        self.lbl.move(130,20)

        vbox.addWidget(lbl)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Font dialog')
        self.show()

    def showDialog(self):
        font,ok=QtGui.QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)

 
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()



