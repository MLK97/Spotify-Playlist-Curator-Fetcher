#!/usr/bin/env python

"""Main Functionality of Program

Run this file to start the program.
It connectes the Spotify Playlist Search Algorithm with the GUI
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5 import QtGui
from gui_main import Ui_SPCF
from spotify_search import search

__author__ = "Maximilian Konrad"
__copyright__ = "Copyright 2020, SPCF-Project"
__credits__ = ["Maximilian Konrad", "Rainer Endre"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Maximilian Konrad"
__email__ = "fysikbeats@hotmail.com"
__status__ = "Development"


class MainWindow(QMainWindow):
    result = 'empty'
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setFixedSize(510, 700)

        # set up the interface from desinger
        self.ui = Ui_SPCF()
        self.ui.setupUi(self)

        # event handling
        self.ui.search_button.clicked.connect(self.button_click) # start spotify_search when search_button clicked
        self.ui.main_results.itemClicked.connect(self.on_element_click) # open pop-up when item of main_results clicked

        # add menubar
        self.statusBar() # doesn't work yet

        # display gui
        self.show()

        # set windowTitle and windowIcon
        self.setWindowTitle("SPCF - Spotify Playlist Curator Fetcher")
        app.setWindowIcon(QtGui.QIcon('spotify-logo.png'))


    # adds result to QListWidget
    def add_result(self, result):
        try:
            if(type(result) == str):
                self.ui.main_results.addItem(result)
            else:
                for elem in result:
                    self.ui.main_results.addItem(elem['title'])
        except TypeError:
            print("Error on line {}".format(sys.exc_info()))


    # when element is QListWidget is clicked
    def on_element_click(self):
        w1 = QLabel("Pop-Up")
        w1.show()


    # when search_button is clicked
    def button_click(self):
        global result
        self.ui.main_results.clear() # maybe add unique add instead
        shost = self.ui.search_field.text()
        result = search(shost.split(","))
        self.add_result(result)



app = QApplication(sys.argv)
GUI = MainWindow()
sys.exit(app.exec_())
