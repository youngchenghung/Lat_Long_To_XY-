# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_LatLongXY.ui'
#
# Created: Tue Feb 12 14:36:58 2019
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_LatLongXY(object):
    def setupUi(self, LatLongXY):
        LatLongXY.setObjectName(_fromUtf8("LatLongXY"))
        LatLongXY.resize(363, 190)
        self.groupBox = QtGui.QGroupBox(LatLongXY)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 321, 111))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_Latitude = QtGui.QLabel(self.groupBox)
        self.label_Latitude.setGeometry(QtCore.QRect(10, 60, 152, 32))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Unicode MS"))
        font.setPointSize(12)
        self.label_Latitude.setFont(font)
        self.label_Latitude.setFrameShape(QtGui.QFrame.Box)
        self.label_Latitude.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Latitude.setObjectName(_fromUtf8("label_Latitude"))
        self.label_Longitude = QtGui.QLabel(self.groupBox)
        self.label_Longitude.setGeometry(QtCore.QRect(10, 20, 152, 32))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Unicode MS"))
        font.setPointSize(12)
        self.label_Longitude.setFont(font)
        self.label_Longitude.setFrameShape(QtGui.QFrame.Box)
        self.label_Longitude.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Longitude.setObjectName(_fromUtf8("label_Longitude"))
        self.Longitude_x = QtGui.QLineEdit(self.groupBox)
        self.Longitude_x.setGeometry(QtCore.QRect(170, 20, 136, 32))
        self.Longitude_x.setObjectName(_fromUtf8("Longitude_x"))
        self.Latitude_y = QtGui.QLineEdit(self.groupBox)
        self.Latitude_y.setGeometry(QtCore.QRect(170, 60, 136, 32))
        self.Latitude_y.setObjectName(_fromUtf8("Latitude_y"))
        self.positioning = QtGui.QPushButton(LatLongXY)
        self.positioning.setGeometry(QtCore.QRect(90, 140, 81, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Unicode MS"))
        self.positioning.setFont(font)
        self.positioning.setObjectName(_fromUtf8("positioning"))
        self.cancel = QtGui.QDialogButtonBox(LatLongXY)
        self.cancel.setGeometry(QtCore.QRect(180, 140, 81, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Unicode MS"))
        font.setPointSize(12)
        self.cancel.setFont(font)
        self.cancel.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.Taiwan))
        self.cancel.setOrientation(QtCore.Qt.Horizontal)
        self.cancel.setStandardButtons(QtGui.QDialogButtonBox.Cancel)
        self.cancel.setObjectName(_fromUtf8("cancel"))

        self.retranslateUi(LatLongXY)
        QtCore.QMetaObject.connectSlotsByName(LatLongXY)

    def retranslateUi(self, LatLongXY):
        LatLongXY.setWindowTitle(_translate("LatLongXY", "經緯度定位", None))
        self.label_Latitude.setText(_translate("LatLongXY", "<html><head/><body><p align=\"center\">緯度( Latitude )</p></body></html>", None))
        self.label_Longitude.setText(_translate("LatLongXY", "<html><head/><body><p align=\"center\">經度 ( Longitude )</p></body></html>", None))
        self.positioning.setText(_translate("LatLongXY", "定位", None))

