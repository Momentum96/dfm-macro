# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dfm_macro_ui.ui',
# licensing of 'dfm_macro_ui.ui' applies.
#
# Created: Mon Mar 28 14:54:35 2022
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(343, 124)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.start = QtWidgets.QPushButton(Form)
        self.start.setObjectName("start")
        self.horizontalLayout.addWidget(self.start)
        self.end = QtWidgets.QPushButton(Form)
        self.end.setObjectName("end")
        self.horizontalLayout.addWidget(self.end)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 2)
        self.get_image = QtWidgets.QPushButton(Form)
        self.get_image.setObjectName("get_image")
        self.gridLayout.addWidget(self.get_image, 1, 0, 1, 2)
        self.get_pos = QtWidgets.QPushButton(Form)
        self.get_pos.setObjectName("get_pos")
        self.gridLayout.addWidget(self.get_pos, 2, 0, 1, 2)
        self.label = QtWidgets.QLabel(Form)
        self.label.setText("")
        self.label.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(
            QtWidgets.QApplication.translate("Form", "dfm_macro", None, -1)
        )
        self.start.setText(QtWidgets.QApplication.translate("Form", "실행", None, -1))
        self.end.setText(QtWidgets.QApplication.translate("Form", "종료", None, -1))
        self.get_image.setText(
            QtWidgets.QApplication.translate("Form", "구매 항목 이미지 가져오기", None, -1)
        )
        self.get_pos.setText(
            QtWidgets.QApplication.translate("Form", "클릭 좌표 가져오기", None, -1)
        )
