# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weiboFetch.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_Fetch(object):
    def setupUi(self, Fetch):
        Fetch.setObjectName("Fetch")
        Fetch.resize(439, 292)
        self.centralwidget = QtWidgets.QWidget(Fetch)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 40, 61, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 140, 71, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(200, 39, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 140, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 200, 191, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 90, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 80, 71, 31))
        self.label_3.setObjectName("label_3")
        Fetch.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Fetch)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 439, 23))
        self.menubar.setObjectName("menubar")
        Fetch.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Fetch)
        self.statusbar.setObjectName("statusbar")
        Fetch.setStatusBar(self.statusbar)

        self.retranslateUi(Fetch)
        QtCore.QMetaObject.connectSlotsByName(Fetch)

    def retranslateUi(self, Fetch):
        _translate = QtCore.QCoreApplication.translate
        Fetch.setWindowTitle(_translate("Fetch", "MainWindow"))
        self.label.setText(_translate("Fetch", "用户名"))
        self.label_2.setText(_translate("Fetch", "保存地址"))
        self.pushButton.setText(_translate("Fetch", "选择路径..."))
        self.pushButton_2.setText(_translate("Fetch", "确定"))
        self.label_3.setText(_translate("Fetch", "期望下载页数"))
