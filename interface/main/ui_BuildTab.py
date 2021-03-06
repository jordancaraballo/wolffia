# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buildTab.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_buildTab(object):
    def setupUi(self, buildTab):
        buildTab.setObjectName("buildTab")
        buildTab.resize(1043, 604)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(buildTab.sizePolicy().hasHeightForWidth())
        buildTab.setSizePolicy(sizePolicy)
        buildTab.setMinimumSize(QtCore.QSize(0, 0))
        self.gridLayout = QtWidgets.QGridLayout(buildTab)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(buildTab)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.molCatalog = QtWidgets.QTreeWidget(buildTab)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.molCatalog.setFont(font)
        self.molCatalog.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.molCatalog.setDragEnabled(True)
        self.molCatalog.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.molCatalog.setAlternatingRowColors(False)
        self.molCatalog.setObjectName("molCatalog")
        item_0 = QtWidgets.QTreeWidgetItem(self.molCatalog)
        self.molCatalog.topLevelItem(0).setText(0, "Polymer")
        item_0.setFlags(QtCore.Qt.ItemIsEnabled)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.molCatalog.topLevelItem(0).child(0).setText(0, "Copolymer")
        item_1.setFlags(QtCore.Qt.ItemIsEnabled)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        self.molCatalog.topLevelItem(0).child(0).child(1).setText(0, "Polyaniline")
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.molCatalog.topLevelItem(0).child(1).setText(0, "Homopolymer")
        item_1.setFlags(QtCore.Qt.ItemIsEnabled)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        self.molCatalog.topLevelItem(0).child(1).child(0).setText(0, "PolyADE")
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        self.molCatalog.topLevelItem(0).child(1).child(1).setText(0, "PolyCYT")
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        self.molCatalog.topLevelItem(0).child(1).child(2).setText(0, "PolyGUA")
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        self.molCatalog.topLevelItem(0).child(1).child(3).setText(0, "PolyTHY")
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        self.molCatalog.topLevelItem(0).child(1).child(4).setText(0, "PMMA")
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_0 = QtWidgets.QTreeWidgetItem(self.molCatalog)
        self.molCatalog.topLevelItem(1).setText(0, "Carbon Allotrope")
        item_0.setFlags(QtCore.Qt.ItemIsEnabled)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.molCatalog.topLevelItem(1).child(0).setText(0, "swCNT")
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.molCatalog.topLevelItem(1).child(1).setText(0, "Graphene")
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.molCatalog)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.molCatalog)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_0 = QtWidgets.QTreeWidgetItem(self.molCatalog)
        self.molCatalog.topLevelItem(4).setText(0, "Solvent")
        item_0.setFlags(QtCore.Qt.ItemIsEnabled)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setFlags(QtCore.Qt.ItemIsEnabled)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setFlags(QtCore.Qt.ItemIsEnabled)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.molCatalog.topLevelItem(4).child(2).setText(0, "Chloroform")
        item_1.setFlags(QtCore.Qt.ItemIsEnabled)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setFlags(QtCore.Qt.ItemIsEnabled)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setFlags(QtCore.Qt.ItemIsEnabled)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setFlags(QtCore.Qt.ItemIsEnabled)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.molCatalog.topLevelItem(4).child(7).setText(0, "Water")
        item_1.setFlags(QtCore.Qt.ItemIsEnabled)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setFlags(QtCore.Qt.ItemIsEnabled)
        item_0 = QtWidgets.QTreeWidgetItem(self.molCatalog)
        self.verticalLayout.addWidget(self.molCatalog)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_2 = QtWidgets.QLabel(buildTab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_15.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.catalogButton = QtWidgets.QPushButton(buildTab)
        self.catalogButton.setObjectName("catalogButton")
        self.horizontalLayout.addWidget(self.catalogButton)
        self.copyButton = QtWidgets.QPushButton(buildTab)
        self.copyButton.setText("")
        self.copyButton.setObjectName("copyButton")
        self.horizontalLayout.addWidget(self.copyButton)
        self.removeButton = QtWidgets.QPushButton(buildTab)
        self.removeButton.setText("")
        self.removeButton.setObjectName("removeButton")
        self.horizontalLayout.addWidget(self.removeButton)
        self.duplicateButton = QtWidgets.QPushButton(buildTab)
        self.duplicateButton.setText("")
        self.duplicateButton.setObjectName("duplicateButton")
        self.horizontalLayout.addWidget(self.duplicateButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.addCustomButton = QtWidgets.QPushButton(buildTab)
        self.addCustomButton.setText("")
        self.addCustomButton.setObjectName("addCustomButton")
        self.horizontalLayout.addWidget(self.addCustomButton)
        self.saveWFMbutton = QtWidgets.QPushButton(buildTab)
        self.saveWFMbutton.setText("")
        self.saveWFMbutton.setObjectName("saveWFMbutton")
        self.horizontalLayout.addWidget(self.saveWFMbutton)
        self.updateButton = QtWidgets.QPushButton(buildTab)
        self.updateButton.setText("")
        self.updateButton.setObjectName("updateButton")
        self.horizontalLayout.addWidget(self.updateButton)
        self.verticalLayout_15.addLayout(self.horizontalLayout)
        self.structManager = QtWidgets.QTableWidget(buildTab)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.structManager.setFont(font)
        self.structManager.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.structManager.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.structManager.setObjectName("structManager")
        self.structManager.setColumnCount(5)
        self.structManager.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.structManager.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.structManager.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Name")
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.structManager.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Atoms")
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.structManager.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("ID")
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.structManager.setHorizontalHeaderItem(4, item)
        self.verticalLayout_15.addWidget(self.structManager)
        self.structPropertyLabel = QtWidgets.QLabel(buildTab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.structPropertyLabel.setFont(font)
        self.structPropertyLabel.setObjectName("structPropertyLabel")
        self.verticalLayout_15.addWidget(self.structPropertyLabel)
        self.editorLayout = QtWidgets.QVBoxLayout()
        self.editorLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.editorLayout.setObjectName("editorLayout")
        self.verticalLayout_15.addLayout(self.editorLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_15)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(buildTab)
        QtCore.QMetaObject.connectSlotsByName(buildTab)

    def retranslateUi(self, buildTab):
        _translate = QtCore.QCoreApplication.translate
        buildTab.setWindowTitle(_translate("buildTab", "Dialog"))
        self.label.setText(_translate("buildTab", "Build or Modify structure files"))
        self.molCatalog.setToolTip(_translate("buildTab", "Molecular Stucture Catalog"))
        self.molCatalog.setStatusTip(_translate("buildTab", "Select molecular structures by double clicking over selection."))
        self.molCatalog.headerItem().setText(0, _translate("buildTab", "Molecular Structure Catalog"))
        __sortingEnabled = self.molCatalog.isSortingEnabled()
        self.molCatalog.setSortingEnabled(False)
        self.molCatalog.topLevelItem(0).child(0).child(0).setText(0, _translate("buildTab", "PEDOT"))
        self.molCatalog.topLevelItem(0).child(0).child(2).setText(0, _translate("buildTab", "PSS"))
        self.molCatalog.topLevelItem(0).child(1).child(5).setText(0, _translate("buildTab", "Chitosan"))
        self.molCatalog.topLevelItem(0).child(1).child(6).setText(0, _translate("buildTab", "Polystyrene"))
        self.molCatalog.topLevelItem(0).child(1).child(7).setText(0, _translate("buildTab", "Cellulose"))
        self.molCatalog.topLevelItem(1).child(2).setText(0, _translate("buildTab", "Diamond"))
        self.molCatalog.topLevelItem(1).child(3).setText(0, _translate("buildTab", "Fullerenes"))
        self.molCatalog.topLevelItem(2).setText(0, _translate("buildTab", "Surfactant"))
        self.molCatalog.topLevelItem(2).child(0).setText(0, _translate("buildTab", "SDS"))
        self.molCatalog.topLevelItem(2).child(1).setText(0, _translate("buildTab", "SDBS"))
        self.molCatalog.topLevelItem(2).child(2).setText(0, _translate("buildTab", "PABA-Tetradecane"))
        self.molCatalog.topLevelItem(2).child(3).setText(0, _translate("buildTab", "PABA-Heptane"))
        self.molCatalog.topLevelItem(2).child(4).setText(0, _translate("buildTab", "PABA-Pentane"))
        self.molCatalog.topLevelItem(3).setText(0, _translate("buildTab", "Elements"))
        self.molCatalog.topLevelItem(3).child(0).setText(0, _translate("buildTab", "A through Z"))
        self.molCatalog.topLevelItem(3).child(0).child(0).setText(0, _translate("buildTab", "Argon (Ar)"))
        self.molCatalog.topLevelItem(3).child(0).child(1).setText(0, _translate("buildTab", "Carbon (C)"))
        self.molCatalog.topLevelItem(3).child(0).child(2).setText(0, _translate("buildTab", "Chlorine (Cl)"))
        self.molCatalog.topLevelItem(3).child(0).child(3).setText(0, _translate("buildTab", "Fluorine (F)"))
        self.molCatalog.topLevelItem(3).child(0).child(4).setText(0, _translate("buildTab", "Hydrogen (H)"))
        self.molCatalog.topLevelItem(3).child(0).child(5).setText(0, _translate("buildTab", "Nitrogen (N)"))
        self.molCatalog.topLevelItem(3).child(0).child(6).setText(0, _translate("buildTab", "Oxygen (O)"))
        self.molCatalog.topLevelItem(3).child(0).child(7).setText(0, _translate("buildTab", "Phosphorous (P)"))
        self.molCatalog.topLevelItem(3).child(0).child(8).setText(0, _translate("buildTab", "Sodium (Na)"))
        self.molCatalog.topLevelItem(3).child(0).child(9).setText(0, _translate("buildTab", "Sulfur (S)"))
        self.molCatalog.topLevelItem(4).child(0).setText(0, _translate("buildTab", "AcetoneAllH"))
        self.molCatalog.topLevelItem(4).child(1).setText(0, _translate("buildTab", "AcetoneNoH"))
        self.molCatalog.topLevelItem(4).child(3).setText(0, _translate("buildTab", "Chloroform (4 atoms)"))
        self.molCatalog.topLevelItem(4).child(4).setText(0, _translate("buildTab", "DMF"))
        self.molCatalog.topLevelItem(4).child(5).setText(0, _translate("buildTab", "Hydrogen Peroxide"))
        self.molCatalog.topLevelItem(4).child(6).setText(0, _translate("buildTab", "THF"))
        self.molCatalog.topLevelItem(4).child(8).setText(0, _translate("buildTab", "Xylene"))
        self.molCatalog.topLevelItem(5).setText(0, _translate("buildTab", "Custom"))
        self.molCatalog.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("buildTab", "Manage Molecular Structures"))
        self.catalogButton.setText(_translate("buildTab", "<--"))
        self.copyButton.setToolTip(_translate("buildTab", "Copy"))
        self.removeButton.setToolTip(_translate("buildTab", "Cut"))
        self.duplicateButton.setToolTip(_translate("buildTab", "Paste"))
        self.addCustomButton.setToolTip(_translate("buildTab", "Load Molecule."))
        self.saveWFMbutton.setToolTip(_translate("buildTab", "Save the mixture without."))
        self.updateButton.setToolTip(_translate("buildTab", "Update coordinates"))
        self.structManager.setSortingEnabled(True)
        item = self.structManager.horizontalHeaderItem(0)
        item.setToolTip(_translate("buildTab", "Show/hide molecules"))
        item = self.structManager.horizontalHeaderItem(1)
        item.setToolTip(_translate("buildTab", "Fix/loose molecule"))
        item = self.structManager.horizontalHeaderItem(2)
        item.setToolTip(_translate("buildTab", "Unique identifier associated to each molecule"))
        item = self.structManager.horizontalHeaderItem(3)
        item.setToolTip(_translate("buildTab", "Atom count"))
        item = self.structManager.horizontalHeaderItem(4)
        item.setToolTip(_translate("buildTab", "Name of molecular structure"))
        self.structPropertyLabel.setText(_translate("buildTab", "Property Editor"))

