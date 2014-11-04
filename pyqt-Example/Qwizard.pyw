#!/usr/bin/python 
from PyQt4 import QtGui


def createIntroPage():
    page = QtGui.QWizardPage()
    page.setTitle("Introduction")

    label = QtGui.QLabel("This wizard will help you register your copy of ")
    label.setWordWrap(True)

    layout = QtGui.QVBoxLayout()
    layout.addWidget(label)
    page.setLayout(layout)
    return page


def createRegistrationPage():
    page = QtGui.QWizardPage()
    page.setTitle("Registration")
    page.setSubTitle("Please fill both fields.")

    nameLabel = QtGui.QLabel("Name:")
    nameLineEdit = QtGui.QLineEdit()

    emailLabel = QtGui.QLabel("Email address:")
    emailLineEdit = QtGui.QLineEdit()

    nameLabel1 = QtGui.QLabel("Name:")                                           
    nameLineEdit1 = QtGui.QLineEdit()
    
    nameLabel2 = QtGui.QLabel("Name:")                                           
    nameLineEdit2 = QtGui.QLineEdit()
    
    nameLabel3 = QtGui.QLabel("Name:")                                           
    nameLineEdit3 = QtGui.QLineEdit() 
    
    nameLabel4 = QtGui.QLabel("Name:")                                           
    nameLineEdit4 = QtGui.QLineEdit()           

    nameLabel5 = QtGui.QLabel("Name:")                                           
    nameLineEdit5 = QtGui.QLineEdit()   
    
    nameLabel6 = QtGui.QLabel("Name:")                                          
    nameLineEdit6 = QtGui.QLineEdit()
    nameLabel7 = QtGui.QLabel("Name:")                                          
    nameLineEdit7 = QtGui.QLineEdit()
    nameLabel8 = QtGui.QLabel("Name:")                                          
    nameLineEdit8 = QtGui.QLineEdit()
    nameLabel9 = QtGui.QLabel("Name:")                                          
    nameLineEdit9 = QtGui.QLineEdit()
    nameLabel10 = QtGui.QLabel("Name:")                                          
    nameLineEdit10 = QtGui.QLineEdit()    
    nameLabel11 = QtGui.QLabel("Name:")                                          
    nameLineEdit11 = QtGui.QLineEdit()    
    nameLabel12 = QtGui.QLabel("Name:")                                          
    nameLineEdit12 = QtGui.QLineEdit()    
    nameLabel13 = QtGui.QLabel("Name:")                                          
    nameLineEdit13 = QtGui.QLineEdit()    
    nameLabel14 = QtGui.QLabel("Name:")                                          
    nameLineEdit14 = QtGui.QLineEdit()    
    nameLabel15 = QtGui.QLabel("Name:")                                          
    nameLineEdit15 = QtGui.QLineEdit()    
    nameLabel16 = QtGui.QLabel("Name:")                                          
    nameLineEdit16 = QtGui.QLineEdit()    
    layout = QtGui.QGridLayout()
    layout.addWidget(nameLabel, 0, 0)
    layout.addWidget(nameLineEdit, 0, 1)
    layout.addWidget(emailLabel, 1, 0)
    layout.addWidget(emailLineEdit, 1, 1)
    layout.addWidget(nameLabel1, 2, 0)                                           
    layout.addWidget(nameLineEdit1, 2, 1) 
    layout.addWidget(nameLabel2, 3, 0)                                           
    layout.addWidget(nameLineEdit2, 3, 1) 
    layout.addWidget(nameLabel3, 4, 0)                                           
    layout.addWidget(nameLineEdit3, 4, 1) 
    layout.addWidget(nameLabel4, 5, 0)                                           
    layout.addWidget(nameLineEdit4, 5, 1) 
    layout.addWidget(nameLabel5, 6, 0)                                           
    layout.addWidget(nameLineEdit5, 6, 1)
    layout.addWidget(nameLabel6, 7, 0)                                          
    layout.addWidget(nameLineEdit6, 7, 1)
    layout.addWidget(nameLabel7, 8, 0)                                          
    layout.addWidget(nameLineEdit7, 8, 1)
    layout.addWidget(nameLabel8, 9, 0)                                          
    layout.addWidget(nameLineEdit8, 9, 1) 
    layout.addWidget(nameLabel9, 10, 0)                                          
    layout.addWidget(nameLineEdit9, 10, 1)     
    layout.addWidget(nameLabel10, 11, 0)                                          
    layout.addWidget(nameLineEdit10, 11, 1)     
    layout.addWidget(nameLabel11, 12, 0)                                          
    layout.addWidget(nameLineEdit11, 12, 1)     
    layout.addWidget(nameLabel12, 13, 0)                                          
    layout.addWidget(nameLineEdit12, 13, 1)     
    layout.addWidget(nameLabel13, 14, 0)                                          
    layout.addWidget(nameLineEdit13, 14, 1)     
    layout.addWidget(nameLabel14, 15, 0)                                          
    layout.addWidget(nameLineEdit14, 15, 1)     
    layout.addWidget(nameLabel15, 16, 0)                                          
    layout.addWidget(nameLineEdit15, 16, 1)     
    layout.addWidget(nameLabel16, 17, 0)                                          
    layout.addWidget(nameLineEdit16, 17, 1)     

    page.setLayout(layout)
    return page


def createConclusionPage():
    page = QtGui.QWizardPage()
    page.setTitle("Conclusion")
    label = QtGui.QLabel("You are now successfully registered. Have a nice day!")
    label.setWordWrap(True)

    layout = QtGui.QVBoxLayout()
    layout.addWidget(label)
    page.setLayout(layout)
    return page


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    wizard = QtGui.QWizard()
    wizard.addPage(createIntroPage())
    wizard.addPage(createRegistrationPage())
    wizard.addPage(createConclusionPage())
    wizard.setWindowTitle("Trivial Wizard")
    wizard.show()
    sys.exit(wizard.exec_())
    
