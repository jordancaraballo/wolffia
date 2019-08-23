# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'minTab.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_minTab(object):
    def setupUi(self, minTab):
        minTab.setObjectName("minTab")
        minTab.resize(1119, 530)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(minTab.sizePolicy().hasHeightForWidth())
        minTab.setSizePolicy(sizePolicy)
        minTab.setMinimumSize(QtCore.QSize(0, 0))
        self.gridLayout = QtWidgets.QGridLayout(minTab)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.minTree = QtWidgets.QTreeWidget(minTab)
        self.minTree.setStyleSheet("font: 11pt \"Ubuntu\";")
        self.minTree.setObjectName("minTree")
        self.minTree.headerItem().setTextAlignment(0, QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.minTree.headerItem().setForeground(0, brush)
        self.minTree.headerItem().setTextAlignment(1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        item_0 = QtWidgets.QTreeWidgetItem(self.minTree)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.minTree)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.minTree.header().setDefaultSectionSize(250)
        self.verticalLayout_2.addWidget(self.minTree)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.resetButton = QtWidgets.QPushButton(minTab)
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout_2.addWidget(self.resetButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.minButton = QtWidgets.QPushButton(minTab)
        self.minButton.setObjectName("minButton")
        self.horizontalLayout_2.addWidget(self.minButton)
        self.stopButton = QtWidgets.QPushButton(minTab)
        self.stopButton.setEnabled(False)
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout_2.addWidget(self.stopButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(minTab)
        QtCore.QMetaObject.connectSlotsByName(minTab)

    def retranslateUi(self, minTab):
        _translate = QtCore.QCoreApplication.translate
        minTab.setWindowTitle(_translate("minTab", "Dialog"))
        self.minTree.headerItem().setText(0, _translate("minTab", "Value"))
        self.minTree.headerItem().setText(1, _translate("minTab", "Parameters"))
        __sortingEnabled = self.minTree.isSortingEnabled()
        self.minTree.setSortingEnabled(False)
        self.minTree.topLevelItem(0).setText(0, _translate("minTab", "Minimizer parameters"))
        self.minTree.topLevelItem(0).child(0).setText(1, _translate("minTab", "Steps"))
        self.minTree.topLevelItem(0).child(1).setText(1, _translate("minTab", "First initial step for line minimizer"))
        self.minTree.topLevelItem(0).child(2).setText(1, _translate("minTab", "Max initial step for line minimizer"))
        self.minTree.topLevelItem(0).child(3).setText(1, _translate("minTab", "Gradient reduction factor for line minimizer"))
        self.minTree.topLevelItem(1).setText(0, _translate("minTab", "Nonbonded interactions"))
        self.minTree.topLevelItem(1).child(0).setText(1, _translate("minTab", "Exclusion for atoms with distances"))
        self.minTree.topLevelItem(1).child(1).setText(1, _translate("minTab", "Scaling factor for 1-4 interactions"))
        self.minTree.topLevelItem(1).child(2).setText(1, _translate("minTab", "Cuttoff distance"))
        self.minTree.topLevelItem(1).child(3).setText(1, _translate("minTab", "Use switching Function"))
        self.minTree.topLevelItem(1).child(4).setText(1, _translate("minTab", "Distance to activate switching function"))
        self.minTree.topLevelItem(1).child(5).setText(1, _translate("minTab", "Distance for inclusion in pair lists"))
        self.minTree.setSortingEnabled(__sortingEnabled)
        self.resetButton.setText(_translate("minTab", "Reset to Defaults"))
        self.minButton.setText(_translate("minTab", "Run"))
        self.stopButton.setText(_translate("minTab", "Stop"))
