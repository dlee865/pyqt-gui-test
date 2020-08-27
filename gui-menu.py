# Author: Dylan Lee
# File: gui-menu.py
# Description:
#   Simple GUI application built using PyQt5 
#   to serve as an example for CS340-Fall2020

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
import sys

# create an instance of a QApplication
app = QApplication(sys.argv)


display_window = QWidget()
display_window.setWindowTitle("Test PyQt5 GUI App")
display_window.setGeometry(300,300,200,80)
display_window.move(60,15)
helloMsg = QLabel('<h1> Hello World! <h1>', parent=window)
helloMsg.move(60,15)

display_window.show()

sys.exit(app.exec_())