# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'playlist_detail.ui'
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
        self.main_title.setMaximumSize(QtCore.QSize(500, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.main_title.setFont(font)
        self.main_title.setAlignment(QtCore.Qt.AlignCenter)
        self.main_title.setObjectName("main_title")
        self.main_functions.addWidget(self.main_title)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setMaximumSize(QtCore.QSize(500, 40))
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.textEdit_2 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_2.setMaximumSize(QtCore.QSize(500, 40))
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout.addWidget(self.textEdit_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.textEdit_3 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_3.setMaximumSize(QtCore.QSize(500, 40))
        self.textEdit_3.setObjectName("textEdit_3")
        self.verticalLayout.addWidget(self.textEdit_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.textEdit_4 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_4.setMaximumSize(QtCore.QSize(500, 16777215))
        self.textEdit_4.setObjectName("textEdit_4")
        self.verticalLayout.addWidget(self.textEdit_4)
        self.main_functions.addLayout(self.verticalLayout)
        SPCF.setCentralWidget(self.main_frame)
        self.statusbar = QtWidgets.QStatusBar(SPCF)
        self.statusbar.setObjectName("statusbar")
        SPCF.setStatusBar(self.statusbar)

        self.retranslateUi(SPCF)
        QtCore.QMetaObject.connectSlotsByName(SPCF)

    def retranslateUi(self, SPCF):
        _translate = QtCore.QCoreApplication.translate
        SPCF.setWindowTitle(_translate("SPCF", "MainWindow"))
        self.main_title.setText(_translate("SPCF", "SPOTIFY PLAYLIST CURATOR FETCHER"))
        self.label.setText(_translate("SPCF", "Title:"))
        self.label_2.setText(_translate("SPCF", "E-Mail:"))
        self.label_3.setText(_translate("SPCF", "URL:"))
        self.label_4.setText(_translate("SPCF", "Description:"))
