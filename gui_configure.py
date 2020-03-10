# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configure.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SPCF(object):
    def setupUi(self, SPCF):
        SPCF.setObjectName("SPCF")
        SPCF.resize(500, 700)
        SPCF.setStyleSheet("background: #282828;\n"
"color: #000000;\n"
"")
        self.main_frame = QtWidgets.QWidget(SPCF)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.main_frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 481, 661))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.main_functions = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.main_functions.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.main_functions.setContentsMargins(10, 5, 10, 5)
        self.main_functions.setSpacing(10)
        self.main_functions.setObjectName("main_functions")
        self.main_title = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.main_title.setMaximumSize(QtCore.QSize(500, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono for Powerline")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.main_title.setFont(font)
        self.main_title.setStyleSheet("color:#ffffff;\n"
"padding: 10px 10px 10px 10px")
        self.main_title.setAlignment(QtCore.Qt.AlignCenter)
        self.main_title.setObjectName("main_title")
        self.main_functions.addWidget(self.main_title)
        self.instruction_field = KTextBrowser(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.instruction_field.setFont(font)
        self.instruction_field.setStyleSheet("")
        self.instruction_field.setObjectName("instruction_field")
        self.main_functions.addWidget(self.instruction_field)
        self.identity_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.identity_label.setFont(font)
        self.identity_label.setStyleSheet("color: #ffffff")
        self.identity_label.setObjectName("identity_label")
        self.main_functions.addWidget(self.identity_label)
        self.identity_field = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.identity_field.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.identity_field.setFont(font)
        self.identity_field.setStyleSheet("background:#FFFFFF;\n"
"color: #000000;\n"
"padding: 10px 10px 10px 10px;\n"
"border-radius: 20px;")
        self.identity_field.setText("")
        self.identity_field.setObjectName("identity_field")
        self.main_functions.addWidget(self.identity_field)
        self.secret_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.secret_label.setFont(font)
        self.secret_label.setStyleSheet("color: #ffffff")
        self.secret_label.setObjectName("secret_label")
        self.main_functions.addWidget(self.secret_label)
        self.secret_field = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.secret_field.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.secret_field.setFont(font)
        self.secret_field.setStyleSheet("background:#FFFFFF;\n"
"color: #000000;\n"
"padding: 10px 10px 10px 10px;\n"
"border-radius: 20px;")
        self.secret_field.setText("")
        self.secret_field.setObjectName("secret_field")
        self.main_functions.addWidget(self.secret_field)
        self.secret_label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.secret_label_2.setFont(font)
        self.secret_label_2.setStyleSheet("color: #ffffff")
        self.secret_label_2.setText("")
        self.secret_label_2.setObjectName("secret_label_2")
        self.main_functions.addWidget(self.secret_label_2)
        self.submit_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.submit_button.setMinimumSize(QtCore.QSize(10, 45))
        self.submit_button.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.submit_button.setFont(font)
        self.submit_button.setStyleSheet("border-radius: 20px;\n"
"color: #ffffff;\n"
"background-color: #1ab26b;\n"
"padding: 10px 10px 10px 10px;\n"
"")
        self.submit_button.setObjectName("submit_button")
        self.main_functions.addWidget(self.submit_button)
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
        self.instruction_field.setHtml(_translate("SPCF", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400; color:#ffffff;\"> Before you can start using this app you have to create your own ID and Secret on </span><a href=\"https://developer.spotify.com/dashboard/login\"><span style=\" font-weight:400; text-decoration: underline; color:#ffffff;\">this page</span></a><span style=\" font-weight:400;\">.</span></p></body></html>"))
        self.identity_label.setText(_translate("SPCF", "Identity:"))
        self.secret_label.setText(_translate("SPCF", "Secret:"))
        self.submit_button.setText(_translate("SPCF", "Submit..."))
from ktextbrowser import KTextBrowser
