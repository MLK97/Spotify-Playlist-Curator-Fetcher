#!/usr/bin/env python

"""Main Functionality of Program

Run this file to start the program.
It connectes the Spotify Playlist Search Algorithm with the GUI
"""

import sys
from PyQt5.QtWidgets import QAction, QApplication, QMainWindow, qApp
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
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


class MainWindow(QMainWindow, Ui_SPCF):
    result = 'empty'

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setFixedSize(510, 700)

        # set up the interface from desinger
        self.ui = Ui_SPCF()
        self.ui.setupUi(self)

        # event handling
        self.ui.search_button.clicked.connect(self.search_playlist)
        self.ui.main_results.itemClicked.connect(self.on_element_click)

        # add menubar
        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Configure')
        fileMenu.triggered.connect(self.open_config)

        menubar.setStyleSheet("color:#ffffff")
        font_menu = QtGui.QFont()
        font_menu.setPointSize(10)
        font_menu.setBold(True)
        font_menu.setWeight(75)
        menubar.setFont(font_menu)


        # display gui
        self.show()

        # set windowTitle and windowIcon
        self.setWindowTitle("SPCF - Spotify Playlist Curator Fetcher")


    # Adds result to QListWidget

    def add_result(self, result):
        try:
            if(type(result) == str):
                self.ui.main_results.addItem(result)
            else:
                for elem in result:
                    self.ui.main_results.addItem(elem['title'])
        except TypeError:
            print("Error on line {}".format(sys.exc_info()))

    # When element in QListWidget is clicked
    def on_element_click(self):
        global result
        global current_item
        # self.detail_ui = Ui_playlist_detail()
        # self.detail_ui.setupUi(self)
        self.playlist_detail = PlaylistDetail()
        # self.close()
        selected_item = self.ui.main_results.selectedItems()
        selected_item_title = selected_item[0].text()
        self.playlist_detail.show()
        self.playlist_detail.show_detail(selected_item_title)



    # when search_button is clicked
    def search_playlist(self):
        global result
        self.ui.main_results.clear()  # maybe add unique add instead
        shost = self.ui.search_field.text()
        result = search(shost.split(","))
        self.add_result(result)
        return result

    def open_config(self):
        print("Hello World")


class PlaylistDetail(QMainWindow, Ui_playlist_detail):
    def __init__(self, parent=None):
        super(PlaylistDetail, self).__init__(parent)
        self.setFixedSize(510, 700)

        # set up the interface for playlist_detail
        self.detail_ui = Ui_playlist_detail()
        self.detail_ui.setupUi(self)
        self.show()
        self.detail_ui.back_button.clicked.connect(self.hide)

    def show_detail(self, selected_item_title):
        for elem in result:
            if elem['title'] == selected_item_title:
                self.detail_ui.title_input.setText(str(elem['title']))
                self.detail_ui.email_input.setText(elem['email'])
                for item in elem['url']:
                    self.detail_ui.url_input.setText(str(item))
                self.detail_ui.desc_input.setText(elem['description'])


class Controller:
    def __init__(self):
        pass

    def show_main(self):
        self.window = MainWindow()
        self.window.show()

    def show_playlist_detail(self):
        self.playlist_detail = PlaylistDetail()
        self.window.close()
        self.playlist_detail.show()


def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('spotify-logo.png'))
    controller = Controller()
    controller.show_main()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
