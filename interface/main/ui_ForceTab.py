# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forceTab.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_forceTab(object):
    def setupUi(self, forceTab):
        forceTab.setObjectName("forceTab")
        forceTab.setEnabled(True)
        forceTab.resize(714, 475)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(forceTab.sizePolicy().hasHeightForWidth())
        forceTab.setSizePolicy(sizePolicy)
        forceTab.setMinimumSize(QtCore.QSize(0, 0))
        self.gridLayout = QtWidgets.QGridLayout(forceTab)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(forceTab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.aboutTab = QtWidgets.QToolButton(forceTab)
        self.aboutTab.setObjectName("aboutTab")
        self.horizontalLayout_5.addWidget(self.aboutTab)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.bondButton = QtWidgets.QPushButton(forceTab)
        self.bondButton.setObjectName("bondButton")
        self.horizontalLayout_5.addWidget(self.bondButton)
        self.line_2 = QtWidgets.QFrame(forceTab)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_5.addWidget(self.line_2)
        self.typesButton = QtWidgets.QPushButton(forceTab)
        self.typesButton.setText("")
        self.typesButton.setObjectName("typesButton")
        self.horizontalLayout_5.addWidget(self.typesButton)
        self.findCHARMMButton = QtWidgets.QPushButton(forceTab)
        self.findCHARMMButton.setText("")
        self.findCHARMMButton.setObjectName("findCHARMMButton")
        self.horizontalLayout_5.addWidget(self.findCHARMMButton)
        self.loadButton = QtWidgets.QPushButton(forceTab)
        self.loadButton.setText("")
        self.loadButton.setObjectName("loadButton")
        self.horizontalLayout_5.addWidget(self.loadButton)
        self.saveButton = QtWidgets.QPushButton(forceTab)
        self.saveButton.setEnabled(True)
        self.saveButton.setText("")
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout_5.addWidget(self.saveButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.defaultForField = QtWidgets.QToolBox(forceTab)
        self.defaultForField.setObjectName("defaultForField")
        self.chargesBox = QtWidgets.QWidget()
        self.chargesBox.setGeometry(QtCore.QRect(0, 0, 683, 247))
        self.chargesBox.setObjectName("chargesBox")
        self.gridLayout_33 = QtWidgets.QGridLayout(self.chargesBox)
        self.gridLayout_33.setObjectName("gridLayout_33")
        self.chargesTable = QtWidgets.QTableWidget(self.chargesBox)
        self.chargesTable.setGeometry(QtCore.QRect(0, 0, 681, 251))
        self.chargesTable.setObjectName("chargesTable")
        self.chargesTable.setColumnCount(3)
        self.chargesTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.chargesTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.chargesTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.chargesTable.setHorizontalHeaderItem(2, item)
        self.gridLayout_33.addWidget(self.chargesTable, 0, 0, 1, 1)
        self.defaultForField.addItem(self.chargesBox, "")
        self.nonbondedBox = QtWidgets.QWidget()
        self.nonbondedBox.setGeometry(QtCore.QRect(0, 0, 683, 247))
        self.nonbondedBox.setObjectName("nonbondedBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.nonbondedBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.nonBondTable = QtWidgets.QTableWidget(self.nonbondedBox)
        self.nonBondTable.setObjectName("nonBondTable")
        self.nonBondTable.setColumnCount(3)
        self.nonBondTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.nonBondTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.nonBondTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.nonBondTable.setHorizontalHeaderItem(2, item)
        self.gridLayout_3.addWidget(self.nonBondTable, 0, 0, 1, 1)
        self.defaultForField.addItem(self.nonbondedBox, "")
        self.bondBox = QtWidgets.QWidget()
        self.bondBox.setGeometry(QtCore.QRect(0, 0, 683, 247))
        self.bondBox.setObjectName("bondBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.bondBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.bondsTable = QtWidgets.QTableWidget(self.bondBox)
        self.bondsTable.setObjectName("bondsTable")
        self.bondsTable.setColumnCount(3)
        self.bondsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.bondsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bondsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.bondsTable.setHorizontalHeaderItem(2, item)
        self.gridLayout_2.addWidget(self.bondsTable, 0, 0, 1, 1)
        self.FBonds = QtWidgets.QLabel(self.bondBox)
        self.FBonds.setObjectName("FBonds")
        self.gridLayout_2.addWidget(self.FBonds, 0, 1, 1, 1)
        self.defaultForField.addItem(self.bondBox, "")
        self.anglesBox = QtWidgets.QWidget()
        self.anglesBox.setGeometry(QtCore.QRect(0, 0, 683, 247))
        self.anglesBox.setObjectName("anglesBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.anglesBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.anglesLayout = QtWidgets.QVBoxLayout()
        self.anglesLayout.setObjectName("anglesLayout")
        self.anglesTable = QtWidgets.QTableWidget(self.anglesBox)
        self.anglesTable.setObjectName("anglesTable")
        self.anglesTable.setColumnCount(3)
        self.anglesTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.anglesTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.anglesTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.anglesTable.setHorizontalHeaderItem(2, item)
        self.anglesLayout.addWidget(self.anglesTable)
        self.gridLayout_4.addLayout(self.anglesLayout, 0, 0, 1, 1)
        self.defaultForField.addItem(self.anglesBox, "")
        self.dihedralsBox = QtWidgets.QWidget()
        self.dihedralsBox.setGeometry(QtCore.QRect(0, 0, 683, 247))
        self.dihedralsBox.setObjectName("dihedralsBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.dihedralsBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.dihedralTable = QtWidgets.QTableWidget(self.dihedralsBox)
        self.dihedralTable.setObjectName("dihedralTable")
        self.dihedralTable.setColumnCount(4)
        self.dihedralTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.dihedralTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dihedralTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dihedralTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.dihedralTable.setHorizontalHeaderItem(3, item)
        self.gridLayout_5.addWidget(self.dihedralTable, 0, 0, 1, 1)
        self.defaultForField.addItem(self.dihedralsBox, "")
        self.verticalLayout_7.addWidget(self.defaultForField)
        self.verticalLayout_2.addLayout(self.verticalLayout_7)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(forceTab)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 1, 1, 1)

        self.retranslateUi(forceTab)
        self.defaultForField.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(forceTab)

    def retranslateUi(self, forceTab):
        _translate = QtCore.QCoreApplication.translate
        forceTab.setWindowTitle(_translate("forceTab", "Dialog"))
        self.label.setText(_translate("forceTab", "1  Set force fields"))
        self.aboutTab.setToolTip(_translate("forceTab", "About Tab"))
        self.aboutTab.setText(_translate("forceTab", "?"))
        self.bondButton.setText(_translate("forceTab", "bonds"))
        self.typesButton.setToolTip(_translate("forceTab", "Detect atom types."))
        self.loadButton.setToolTip(_translate("forceTab", "Load PRM File"))
        self.saveButton.setToolTip(_translate("forceTab", "Save PRM File"))
        item = self.chargesTable.horizontalHeaderItem(0)
        item.setText(_translate("forceTab", "Atom"))
        item = self.chargesTable.horizontalHeaderItem(1)
        item.setText(_translate("forceTab", "Type"))
        item = self.chargesTable.horizontalHeaderItem(2)
        item.setText(_translate("forceTab", "Charge"))
        self.defaultForField.setItemText(self.defaultForField.indexOf(self.chargesBox), _translate("forceTab", "ATOMS TYPES AND CHARGES"))
        item = self.nonBondTable.horizontalHeaderItem(0)
        item.setText(_translate("forceTab", "Type"))
        item = self.nonBondTable.horizontalHeaderItem(1)
        item.setText(_translate("forceTab", "e"))
        item = self.nonBondTable.horizontalHeaderItem(2)
        item.setText(_translate("forceTab", "Rmin/2"))
        self.defaultForField.setItemText(self.defaultForField.indexOf(self.nonbondedBox), _translate("forceTab", "NONBONDED"))
        item = self.bondsTable.horizontalHeaderItem(0)
        item.setText(_translate("forceTab", "Type"))
        item = self.bondsTable.horizontalHeaderItem(1)
        item.setText(_translate("forceTab", "Kb"))
        item = self.bondsTable.horizontalHeaderItem(2)
        item.setText(_translate("forceTab", "b0"))
        self.FBonds.setText(_translate("forceTab", "<html><head/><body><p><br/></p></body></html>"))
        self.defaultForField.setItemText(self.defaultForField.indexOf(self.bondBox), _translate("forceTab", "BONDS"))
        item = self.anglesTable.horizontalHeaderItem(0)
        item.setText(_translate("forceTab", "Type"))
        item = self.anglesTable.horizontalHeaderItem(1)
        item.setText(_translate("forceTab", "Ktheta"))
        item = self.anglesTable.horizontalHeaderItem(2)
        item.setText(_translate("forceTab", "Ⲑ0"))
        self.defaultForField.setItemText(self.defaultForField.indexOf(self.anglesBox), _translate("forceTab", "ANGLES"))
        item = self.dihedralTable.horizontalHeaderItem(0)
        item.setText(_translate("forceTab", "Type"))
        item = self.dihedralTable.horizontalHeaderItem(1)
        item.setText(_translate("forceTab", "Kchi"))
        item = self.dihedralTable.horizontalHeaderItem(2)
        item.setText(_translate("forceTab", "n"))
        item = self.dihedralTable.horizontalHeaderItem(3)
        item.setText(_translate("forceTab", "Delta"))
        self.defaultForField.setItemText(self.defaultForField.indexOf(self.dihedralsBox), _translate("forceTab", "DIHEDRALS"))
