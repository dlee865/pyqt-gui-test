# Author: Dylan Lee
# File: gui-example.py
# Description:
#   Simple GUI application built using PyQt5 
#   to serve as an example for CS340-Fall2020

import sys
# import any and all widgets from PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QToolBar
from PyQt5.QtWidgets import QRadioButton
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout

# this class inherits from QMainWindow and will be used to set up the applications GUI
class GUI_Example(QMainWindow):
    def __init__(self):
        super().__init__()
        # give the main application window a name
        self.setWindowTitle('Example GUI Application')
        # set the initial window dimensions
        self.setGeometry(10, 10, 800, 600)
        
        # Rather than use seperate initilization functions (which I would strongly recommend) 
        # I will put code to set up parts of the main window's GUI here
        
        # First lets create a central widget to hold the different parts of our GUI
        # To do this I will create a class variable that is a QWidget object and use that 
        # to then set the central widget for the main window application
        self.central_widget = QWidget(self)
        
        # before fully adding the central widget lets set a layout to keep things organized
        # for this I will just use the standard box layout, but as you will see later you 
        # can nest layouts inside of other layouts
        self.central_layout = QVBoxLayout()

        # now lets create and add some basic widgets to our GUI
        # first a simple text box using QLineEdit
        self.text_box = QLineEdit('Simple Text Box')
        # add it to the layout
        self.central_layout.addWidget(self.text_box)

        # you can create radio buttons
        self.radio_button1 = QRadioButton('Red Pill')
        self.radio_button2 = QRadioButton('Blue Pill')
        # too keep these close togther you can put them in their own layout
        self.rad_layout = QVBoxLayout()
        self.rad_layout.addWidget(self.radio_button1)
        self.rad_layout.addWidget(self.radio_button2)
        # now add that layout to the central 
        self.central_layout.addLayout(self.rad_layout)

        # you can also create push buttons, sometimes easiest done in a loop
        # to keep these well organized you can use a grid layout
        self.grid_layout = QGridLayout()
        for i in range(6):
            self.grid_layout.addWidget(QPushButton('Button ' + str(i)), i/3, i%3)
        # add to central layout
        self.central_layout.addLayout(self.grid_layout)

        # one more widget and layout to look at is the form layout
        self.form_layout = QFormLayout()
        self.form_layout.addRow('First Name:', QLineEdit())
        self.form_layout.addRow('Last Name:', QLineEdit())
        self.form_layout.addRow('Net ID:', QLineEdit())
        # why not through in a combo box for good measure
        self.combo_box = QComboBox()
        self.combo_box.addItems(["Computer Engineering", "Computer Science", "Electrical Engineering"])
        self.form_layout.addRow('Major:', self.combo_box)
        self.central_layout.addLayout(self.form_layout)

        self.central_widget.setLayout(self.central_layout)

        self.setCentralWidget(self.central_widget)
        
        # Time to create a status bar to show whatever info we need too at the bottom of the window
        # this could be handy to display messages to confirm user actions
        self.statusBar().showMessage('Important Status...')
        
        # create the standard menubar toolbar displayed at the top of the window
        menu_bar = self.menuBar()

        # once the menu bar is created we add more menu options
        file_menu = menu_bar.addMenu('File')
        edit_menu = menu_bar.addMenu('Edit')
        view_menu = menu_bar.addMenu('View')
        tool_menu = menu_bar.addMenu('Tools')

        # now to add some options for the menus
        
        # first add a save and exit option in the file menu
        # to make it look snazzier you can get icons for your buttons like this
        save_icon = QIcon.fromTheme('document-save')
        save_button = QAction(save_icon, 'Save', self)
        save_button.setShortcut('Ctrl+S')
        save_button.triggered.connect(self.show_Saved)
        
        exit_icon = QIcon.fromTheme('application-exit')
        exit_button = QAction(exit_icon, 'Quit', self)
        # this binds the button to the macro you choose
        exit_button.setShortcut('Ctrl+Q')
        # this is what actually causes the app to close if exit is clicked
        # this type of connection will be important for buttons with more complex actions
        exit_button.triggered.connect(self.close)
        
        # add the created save and exit button to the file_menu
        file_menu.addAction(save_button)
        file_menu.addAction(exit_button)

        # now a copy and paste option for the edit menu
        copy_icon = QIcon.fromTheme('edit-copy')
        copy_button = QAction(copy_icon, 'Copy', self)
        copy_button.setShortcut('Ctrl+C')
        copy_button.triggered.connect(self.show_Copy)
        
        paste_icon = QIcon.fromTheme('edit-paste')
        paste_button = QAction(paste_icon, 'Paste', self)
        paste_button.setShortcut('Ctrl+V')
        paste_button.triggered.connect(self.show_Paste)
        
        # add the newly made buttons to the edit menu
        edit_menu.addAction(copy_button)
        edit_menu.addAction(paste_button)
        # hopefully this gives you an idea of how to design a toolbar

    # an example of how to bind a function to a triggered action
    # in this case all that happens is the status bar says copied, pasted, saved based on which button they click 
    def show_Saved(self):
        self.statusBar().showMessage('Saved')
    
    def show_Copy(self):
        self.statusBar().showMessage('Copied')
    
    def show_Paste(self):
        self.statusBar().showMessage('Pasted')


def main():
    # declare an instance of the application
    app_example = QApplication(sys.argv)

    # create an instance of the GUI_Example class and display the main window
    main_window = GUI_Example()
    main_window.show()

    # this triggers the event loop for the application
    # calling it inside sys.exit() just ensures a leak free exit
    sys.exit(app_example.exec_())
    
if __name__ == '__main__':
    main()