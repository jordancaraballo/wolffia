# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nanotubeEditor.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NanotubeEditor(object):
    def setupUi(self, NanotubeEditor):
        NanotubeEditor.setObjectName("NanotubeEditor")
        NanotubeEditor.resize(532, 346)
        self.verticalLayoutWidget = QtWidgets.QWidget(NanotubeEditor)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 531, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Nimbus Roman No9 L")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.mSpinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.mSpinBox.setFont(font)
        self.mSpinBox.setMaximum(200)
        self.mSpinBox.setProperty("value", 10)
        self.mSpinBox.setObjectName("mSpinBox")
        self.horizontalLayout_10.addWidget(self.mSpinBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem2)
        self.nSpinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.nSpinBox.setFont(font)
        self.nSpinBox.setMaximum(200)
        self.nSpinBox.setProperty("value", 10)
        self.nSpinBox.setObjectName("nSpinBox")
        self.horizontalLayout_11.addWidget(self.nSpinBox)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_11)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.chiralButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.chiralButton.setChecked(True)
        self.chiralButton.setObjectName("chiralButton")
        self.horizontalLayout_7.addWidget(self.chiralButton)
        self.armchairButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.armchairButton.setObjectName("armchairButton")
        self.horizontalLayout_7.addWidget(self.armchairButton)
        self.zigZagButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.zigZagButton.setObjectName("zigZagButton")
        self.horizontalLayout_7.addWidget(self.zigZagButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Nimbus Roman No9 L")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.tubeLengthSpinBox = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.tubeLengthSpinBox.setDecimals(1)
        self.tubeLengthSpinBox.setMaximum(500.0)
        self.tubeLengthSpinBox.setProperty("value", 20.0)
        self.tubeLengthSpinBox.setObjectName("tubeLengthSpinBox")
        self.horizontalLayout_8.addWidget(self.tubeLengthSpinBox)
        self.horizontalSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.horizontalSlider.setMaximum(4999)
        self.horizontalSlider.setProperty("value", 200)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_8.addWidget(self.horizontalSlider)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.viewerLayout = QtWidgets.QVBoxLayout()
        self.viewerLayout.setObjectName("viewerLayout")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.viewerLayout.addItem(spacerItem6)
        self.horizontalLayout_2.addLayout(self.viewerLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.OKButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.OKButton.setObjectName("OKButton")
        self.horizontalLayout_3.addWidget(self.OKButton)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.cancelButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_3.addWidget(self.cancelButton)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.previewButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.previewButton.setObjectName("previewButton")
        self.horizontalLayout_3.addWidget(self.previewButton)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem11)

        self.retranslateUi(NanotubeEditor)
        QtCore.QMetaObject.connectSlotsByName(NanotubeEditor)

    def retranslateUi(self, NanotubeEditor):
        _translate = QtCore.QCoreApplication.translate
        NanotubeEditor.setWindowTitle(_translate("NanotubeEditor", "Nanotube Editor"))
        self.label_4.setText(_translate("NanotubeEditor", "Nanotube Editor"))
        self.label.setText(_translate("NanotubeEditor", "Chirality"))
        self.label_2.setText(_translate("NanotubeEditor", "m"))
        self.label_3.setText(_translate("NanotubeEditor", "n"))
        self.chiralButton.setText(_translate("NanotubeEditor", "chiral"))
        self.armchairButton.setText(_translate("NanotubeEditor", "armchair"))
        self.zigZagButton.setText(_translate("NanotubeEditor", "zig zag"))
        self.label_5.setText(_translate("NanotubeEditor", "Length (Å)"))
        self.OKButton.setText(_translate("NanotubeEditor", "Save"))
        self.cancelButton.setText(_translate("NanotubeEditor", "Cancel"))
        self.previewButton.setText(_translate("NanotubeEditor", "Preview"))
