#!/usr/bin/env python

"""Main Functionality of Program

Run this file to start the program.
It connectes the Spotify Playlist Search Algorithm with the GUI
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
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

        # add search button_click
        self.ui.search_button.clicked.connect(self.button_click)

        # add menubar
        self.statusBar()

        # display gui
        self.show()

    def button_click(self):
        global result
        shost = self.ui.search_field.text()
        result = search(shost.split(","))
        print(result)
        return result

    # def add_result(self): 


app = QApplication(sys.argv)
GUI = MainWindow()
sys.exit(app.exec_())
