from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt
import sys
import json
import data




class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.__init()

    def changeText(self):
        self.text.setText(self.textField.text())
        self.textField.clear()

    def __init(self):
        self.setWindowTitle("USERS")
        self.setFixedSize(400, 1000)

       
        self.vLayout = QVBoxLayout()
    

        for i in  data.getData():
             self.user = QLabel(i.title+str(i.cb_price),self)
    
             self.user.setStyleSheet("background-color:red;\n")
             self.vLayout.addWidget(self.user)
        self.setLayout(self.vLayout)

       


app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
