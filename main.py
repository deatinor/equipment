import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QDesktopWidget, \
        QPushButton, QMessageBox, QAction, QLineEdit, QLabel
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

        title = QLabel("Hello World from PyQt", self)
        title.setAlignment(QtCore.Qt.AlignCenter)
        gridLayout.addWidget(title, 0, 0)

        qtRectangle=self.frameGeometry()
        centerPoint=QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        print(centerPoint)


        pyButton=QPushButton('Click Me', self)
        pyButton.resize(100,32)
        pyButton.move(50,50)
        pyButton.clicked.connect(self.clickMethod)


        # Create new action
        newAction = QAction(QIcon('new.png'), '&New', self)        
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip('New document')
        newAction.triggered.connect(self.newCall)
 
        # Create new action
        openAction = QAction(QIcon('open.png'), '&Open', self)        
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open document')
        openAction.triggered.connect(self.openCall)
 
 
        # Create menu bar and add action
        menuBar = self.menuBar()
        menuBar.setNativeMenuBar(False)
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)


        self.nameLabel=QLabel(self)
        self.nameLabel.setText('name')
        self.line=QLineEdit(self)
        self.line.move(80,100)
        self.line.resize(200,32)
        self.nameLabel.move(20,100)




        
    def openCall(self):
        print('Open')
        
    def newCall(self):
        print('New')
        
    def exitCall(self):
        print('Exit app')
        

    def clickMethod(self):
        QMessageBox.about(self,'Here',self.line.text())




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HelloWindow()
    mainWin.show()
    sys.exit( app.exec_() )
