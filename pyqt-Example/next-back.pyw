#!/usr/bin/python 

import sys
import os
from PyQt4 import QtGui,QtCore

class MyWizard(QtGui.QWizard):
    def __init__(self,parent=None):
        QtGui.QWizard.__init__(self,parent)
        self.result=0
        self.company_name=""
        self.company_listing=""
        self.info1=""
        self.info2=""
        self.info3=""    
        
        self.setWindowTitle("MyWizard Title")
        self.addPage(company_info(self))
        self.addPage(company_listing(self))
        self.addPage(company_other_infos(self))

        self.finished.connect(self.end)
        pass

    def end(self,result):
        self.result=result 
        if self.result:
                self.company_name = str(self.field("company_name").toString())
                self.company_listing = str(self.field("company_listing").toString())
                self.info1 = str(self.field("info1").toString())
                self.info2 = str(self.field("info2").toString())
                self.info3 = str(self.field("info3").toString())

        print self.company_name
        print self.company_listing
        print self.info1
        print self.info2
        print self.info3

class company_info(QtGui.QWizardPage):
    def __init__(self, parent):
        QtGui.QWizardPage.__init__(self, parent)
        self.setTitle("Step 1/3")
        self.setSubTitle("Company Name")

        # Name
        self.lineEdit = QtGui.QLineEdit("The world company")
        # Fields
        self.registerField("company_name", self.lineEdit)
        # Page layout
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.lineEdit)
        layout.addStretch(1)
        self.setLayout(layout)

    def isComplete(self):
        if self.lineEdit.text() == "The world company":
            self.completeChanged.emit()
            return True
        return False
        
class company_listing(QtGui.QWizardPage):
  def __init__(self, parent):
        QtGui.QWizardPage.__init__(self, parent)
        self.setTitle("Step 2/3")
        self.setSubTitle("Some listing")       
        ipsum = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec a diam lectus. Sed sit amet ipsum mauris.
        Maecenas congue ligula ac quam viverra nec consectetur ante hendrerit. Donec et mollis dolor.
        #Praesent et diam eget libero egestas mattis sit amet vitae augue.
        Nam tincidunt congue enim, ut porta lorem lacinia consectetur. Donec ut libero sed arcu vehicula ultricies a non tortor.
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ut gravida lorem.
        Ut turpis felis, pulvinar a semper sed, adipiscing id dolor. Pellentesque auctor nisi id magna consequat sagittis.
        Curabitur dapibus enim sit amet elit pharetra tincidunt feugiat nisl imperdiet.
        Ut convallis libero in urna ultrices accumsan. Donec sed odio eros.
        Donec viverra mi quis quam pulvinar at malesuada arcu rhoncus.
        Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
        In rutrum accumsan ultricies. Mauris vitae nisi at sem facilisis semper ac in est."""         
                 
        # Some listing in a table widget
        textEdit = QtGui.QTextEdit()
        textEdit.setPlainText(ipsum)
        # Fields
        self.registerField("company_listing", textEdit, "plainText")
        # Page layout
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(textEdit)
        layout.addStretch(1)
        self.setLayout(layout)
        pass

  def initializePage(self):
        pass
  def cleanupPage(self):
        pass

class company_other_infos(QtGui.QWizardPage):
  def __init__(self, parent):
        QtGui.QWizardPage.__init__(self, parent)
        self.setTitle("Step 3/3")
        self.setSubTitle("Other infos")
        # Other infos
        lineEdit_info1 = QtGui.QLineEdit("info1")
        lineEdit_info2 = QtGui.QLineEdit("info2")
        lineEdit_info3 = QtGui.QLineEdit("info3")
        # Fields
        self.registerField("info1", lineEdit_info1)
        self.registerField("info2", lineEdit_info2)
        self.registerField("info3", lineEdit_info3)
        # Page layout
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(lineEdit_info1)
        layout.addWidget(lineEdit_info2)
        layout.addWidget(lineEdit_info3)
        layout.addStretch(1)
        self.setLayout(layout)
                                                             
  def initializePage(self):
        pass
                                                                      
  def cleanupPage(self):
        pass
                                                                                      

app = QtGui.QApplication(sys.argv)
myWizard = MyWizard()
myWizard.show()
sys.exit(app.exec_())        
