from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")
        button.size(100,100)

        self.setFixedSize(QSize(1000, 700))

        # Set the central widget of the Window.
        self.setCentralWidget(button)


class Window(QMainWindow): 
    def __init__(self): 
        super().__init__() 
  
        # setting title 
        self.setWindowTitle("Python ") 
  
        # setting geometry 
        self.setGeometry(1000, 200, 1000, 200) 
  
        # calling method 
        self.UiComponents() 
  
        # showing all the widgets 
        self.show() 
  
    # method for widgets 
    def UiComponents(self): 
  
        # creating a push button 
        button = QPushButton("CLICK", self) 
  
        # setting geometry of button 
        button.setGeometry(200, 150, 200, 150) 
  
  
        # adding action to a button 
        button.clicked.connect(self.clickme) 
  
  
    # action method 
    def clickme(self): 
  
        # printing pressed 
        print("pressed") 
app = QApplication(sys.argv)

window = Window()
window.show()

app.exec()
