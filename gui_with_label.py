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
        SPCF.resize(809, 610)
        self.centralwidget = QtWidgets.QWidget(SPCF)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 80, 761, 491))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.search_button = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.search_button.setObjectName("search_button")
        self.verticalLayout.addWidget(self.search_button)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.results_layout = QtWidgets.QVBoxLayout()
        self.results_layout.setObjectName("results_layout")
        self.results = QtWidgets.QListView(self.verticalLayoutWidget)
        self.results.setObjectName("results")
        self.results_layout.addWidget(self.results)
        self.verticalLayout.addLayout(self.results_layout)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 741, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        SPCF.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SPCF)
        self.statusbar.setObjectName("statusbar")
        SPCF.setStatusBar(self.statusbar)

        self.retranslateUi(SPCF)
        QtCore.QMetaObject.connectSlotsByName(SPCF)

    def retranslateUi(self, SPCF):
        _translate = QtCore.QCoreApplication.translate
        SPCF.setWindowTitle(_translate("SPCF", "MainWindow"))
        self.search_button.setText(_translate("SPCF", "Keyword1, Keyword2, Keyword3"))
        self.pushButton.setText(_translate("SPCF", "Search..."))
        self.label.setText(_translate("SPCF", "SPOTIFY PLAYLIST CURATOR FETCHER"))