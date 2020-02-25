# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'playlist_detail.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_playlist_detail(object):
    def setupUi(self, playlist_detail):
        playlist_detail.setObjectName("playlist_detail")
        playlist_detail.resize(500, 700)
        self.main_frame = QtWidgets.QWidget(playlist_detail)
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
        self.detail_content = QtWidgets.QVBoxLayout()
        self.detail_content.setObjectName("detail_content")
        self.title_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.title_label.setObjectName("title_label")
        self.detail_content.addWidget(self.title_label)
        self.title_input = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.title_input.setMaximumSize(QtCore.QSize(500, 40))
        self.title_input.setReadOnly(True)
        self.title_input.setObjectName("title_input")
        self.detail_content.addWidget(self.title_input)
        self.email_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.email_label.setObjectName("email_label")
        self.detail_content.addWidget(self.email_label)
        self.email_input = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.email_input.setMaximumSize(QtCore.QSize(500, 40))
        self.email_input.setReadOnly(True)
        self.email_input.setObjectName("email_input")
        self.detail_content.addWidget(self.email_input)
        self.url_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.url_label.setObjectName("url_label")
        self.detail_content.addWidget(self.url_label)
        self.url_input = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.url_input.setMaximumSize(QtCore.QSize(500, 40))
        self.url_input.setReadOnly(True)
        self.url_input.setObjectName("url_input")
        self.detail_content.addWidget(self.url_input)
        self.desc_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.desc_label.setObjectName("desc_label")
        self.detail_content.addWidget(self.desc_label)
        self.desc_input = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.desc_input.setMaximumSize(QtCore.QSize(500, 16777215))
        self.desc_input.setReadOnly(True)
        self.desc_input.setObjectName("desc_input")
        self.detail_content.addWidget(self.desc_input)
        self.back_button = QtWidgets.QCommandLinkButton(self.verticalLayoutWidget)
        self.back_button.setObjectName("back_button")
        self.detail_content.addWidget(self.back_button)
        self.main_functions.addLayout(self.detail_content)
        playlist_detail.setCentralWidget(self.main_frame)
        self.statusbar = QtWidgets.QStatusBar(playlist_detail)
        self.statusbar.setObjectName("statusbar")
        playlist_detail.setStatusBar(self.statusbar)

        self.retranslateUi(playlist_detail)
        QtCore.QMetaObject.connectSlotsByName(playlist_detail)

    def retranslateUi(self, playlist_detail):
        _translate = QtCore.QCoreApplication.translate
        playlist_detail.setWindowTitle(_translate("playlist_detail", "MainWindow"))
        self.main_title.setText(_translate("playlist_detail", "SPOTIFY PLAYLIST CURATOR FETCHER"))
        self.title_label.setText(_translate("playlist_detail", "Title:"))
        self.email_label.setText(_translate("playlist_detail", "E-Mail:"))
        self.url_label.setText(_translate("playlist_detail", "URL:"))
        self.desc_label.setText(_translate("playlist_detail", "Description:"))
        self.back_button.setText(_translate("playlist_detail", "Close"))
