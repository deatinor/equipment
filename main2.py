import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QDesktopWidget, \
        QPushButton, QMessageBox, QAction, QLineEdit, QLabel, QDialog, qApp, QHBoxLayout, \
        QVBoxLayout, QTextEdit, QInputDialog, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize    
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui



class HelloWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(640, 480))
        self.setWindowTitle("Hello world")

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        gridLayout = QGridLayout(self)
        centralWidget.setLayout(gridLayout)

        #  title = QLabel("Hello World from PyQt", self)
        #  title.setAlignment(QtCore.Qt.AlignCenter)
        #  gridLayout.addWidget(title, 0, 0)

        left=QDialog()
        buttonsLeft=QDialog()
        buttonsRight=QDialog()
        right=QDialog()
        top=QDialog()

        gridLayout.addWidget(top,0,0,2,2)
        gridLayout.addWidget(buttonsLeft,2,0,1,1)
        gridLayout.addWidget(buttonsRight,2,1,1,1)
        gridLayout.addWidget(left,3,0,8,1)
        gridLayout.addWidget(right,3,1,8,1)



        addEquipmentButton=QPushButton('Add equipment',buttonsLeft)
        addEquipmentButton.clicked.connect(self.addEquipment)
        #  addEquipment.resize()
        addUserButton=QPushButton('Add user',buttonsRight)
        addUserButton.clicked.connect(self.addUser)


        pyButton=QPushButton('Click Me', left)
        pyButton.resize(100,32)
        #  pyButton.move(50,50)
        pyButton.clicked.connect(self.clickMethod)


        pyButton2=QPushButton('Click Me', right)
        pyButton2.resize(100,32)
        #  pyButton.move(50,50)
        pyButton2.clicked.connect(self.clickMethod)


        top.setStyleSheet("QDialog{background-color: pink;}")
        right.setStyleSheet("QDialog{background-color: green;}")
        left.setStyleSheet("QDialog{background-color: red;}")



        self.tableEquipment=QTableWidget(0,1,left)
        #  self.tableEquipment.setSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.tableEquipment.resizeColumnsToContents(1)
        for i in range(0):
            self.tableEquipment.setItem(i,0,QTableWidgetItem(data[i]))

        self.tableUsers=QTableWidget(0,1,right)
        for i in range(0):
            self.tableUsers.setItem(i,0,QTableWidgetItem(data[i]))

        
    
    def clickMethod(self):
        QMessageBox.about(self,'Here','Ciao')


    def addEquipment(self):
        text, ok = QInputDialog.getText(self, 'Equipment Dialog', 
            'Enter the name of the equipment:')
        if ok:
            newRow=self.tableEquipment.rowCount()
            self.tableEquipment.insertRow(newRow)
            self.tableEquipment.setItem(newRow,0,QTableWidgetItem(text))


    def addUser(self):
        text, ok = QInputDialog.getText(self, 'User Dialog', 
            'Enter the name of the user:')
        if ok:
            newRow=self.tableUsers.rowCount()
            self.tableUsers.insertRow(newRow)
            self.tableUsers.setItem(newRow,0,QTableWidgetItem(text))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HelloWindow()
    mainWin.show()
    sys.exit( app.exec_() )
