# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SPCF(object):
    def setupUi(self, SPCF):
        SPCF.setObjectName("SPCF")
        SPCF.resize(500, 700)
        self.main_frame = QtWidgets.QWidget(SPCF)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.main_frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 481, 661))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.main_functions = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.main_functions.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.main_functions.setContentsMargins(0, 0, 0, 0)
        self.main_functions.setSpacing(10)
        self.main_functions.setObjectName("main_functions")
        self.main_title = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.main_title.setFont(font)
        self.main_title.setAlignment(QtCore.Qt.AlignCenter)
        self.main_title.setObjectName("main_title")
        self.main_functions.addWidget(self.main_title)
        self.search_field = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.search_field.setObjectName("search_field")
        self.main_functions.addWidget(self.search_field)
        self.search_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.search_button.setObjectName("search_button")
        self.main_functions.addWidget(self.search_button)
        self.main_results = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.main_results.setObjectName("main_results")
        self.main_functions.addWidget(self.main_results)
        SPCF.setCentralWidget(self.main_frame)
        self.statusbar = QtWidgets.QStatusBar(SPCF)
        self.statusbar.setObjectName("statusbar")
        SPCF.setStatusBar(self.statusbar)

        self.retranslateUi(SPCF)
        QtCore.QMetaObject.connectSlotsByName(SPCF)
        SPCF.setTabOrder(self.search_field, self.search_button)
        SPCF.setTabOrder(self.search_button, self.main_results)

    def retranslateUi(self, SPCF):
        _translate = QtCore.QCoreApplication.translate
        SPCF.setWindowTitle(_translate("SPCF", "MainWindow"))
        self.main_title.setText(_translate("SPCF", "SPOTIFY PLAYLIST CURATOR FETCHER"))
        self.search_field.setText(_translate("SPCF", "Keyword1, Keyword2, Keyword3"))
        self.search_button.setText(_translate("SPCF", "Search..."))
