#!/usr/bin/env python

"""Main Functionality of Program

Run this file to start the program.
It connectes the Spotify Playlist Search Algorithm with the GUI
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui
from gui_main import Ui_SPCF
from gui_playlist_detail import Ui_playlist_detail
from spotify_search import search

__author__ = "Maximilian Konrad"
__copyright__ = "Copyright 2020, SPCF-Project"
__credits__ = ["Maximilian Konrad", "Rainer Endres"]
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
        self.ui.search_button.clicked.connect(self.search_playlist)  # start spotify_search when search_button clicked
        self.ui.main_results.itemClicked.connect(self.on_element_click)  # open pop-up when item of main_results clicked

        # add menubar
        self.statusBar()  # doesn't work yet

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
        global result
        global current_item
        self.detail_ui = Ui_playlist_detail()
        self.detail_ui.setupUi(self)
        selected_item = self.ui.main_results.selectedItems()
        selected_item_title = selected_item[0].text()
        for elem in result:
            if elem['title'] == selected_item_title:
                self.detail_ui.title_input.setText(str(elem['title']))
                self.detail_ui.email_input.setText(elem['email'])
                self.detail_ui.url_input.setText(str(elem['url']))
                self.detail_ui.desc_input.setText(elem['description'])


    # when search_button is clicked
    def search_playlist(self):
        global result
        self.ui.main_results.clear()  # maybe add unique add instead
        shost = self.ui.search_field.text()
        result = search(shost.split(","))
        self.add_result(result)
        return result



app = QApplication(sys.argv)
GUI = MainWindow()
sys.exit(app.exec_())
