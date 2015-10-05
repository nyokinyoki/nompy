# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nompy_about0.2.1.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_aboutDialog(object):
    def setupUi(self, aboutDialog):
        aboutDialog.setObjectName("aboutDialog")
        aboutDialog.resize(418, 246)
        self.verticalLayout = QtWidgets.QVBoxLayout(aboutDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.nompyLabel = QtWidgets.QLabel(aboutDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.nompyLabel.setFont(font)
        self.nompyLabel.setObjectName("nompyLabel")
        self.verticalLayout.addWidget(self.nompyLabel)
        self.versionLabel = QtWidgets.QLabel(aboutDialog)
        self.versionLabel.setObjectName("versionLabel")
        self.verticalLayout.addWidget(self.versionLabel)
        self.aboutLabel = QtWidgets.QLabel(aboutDialog)
        self.aboutLabel.setWordWrap(True)
        self.aboutLabel.setObjectName("aboutLabel")
        self.verticalLayout.addWidget(self.aboutLabel)
        self.copyrightLabel = QtWidgets.QLabel(aboutDialog)
        self.copyrightLabel.setOpenExternalLinks(True)
        self.copyrightLabel.setObjectName("copyrightLabel")
        self.verticalLayout.addWidget(self.copyrightLabel)
        self.licenseLabel = QtWidgets.QLabel(aboutDialog)
        self.licenseLabel.setOpenExternalLinks(True)
        self.licenseLabel.setObjectName("licenseLabel")
        self.verticalLayout.addWidget(self.licenseLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.closeButton = QtWidgets.QPushButton(aboutDialog)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(aboutDialog)
        QtCore.QMetaObject.connectSlotsByName(aboutDialog)

    def retranslateUi(self, aboutDialog):
        _translate = QtCore.QCoreApplication.translate
        aboutDialog.setWindowTitle(_translate("aboutDialog", "About"))
        self.nompyLabel.setText(_translate("aboutDialog", "Nompy"))
        self.versionLabel.setText(_translate("aboutDialog", "Version 0.2.2"))
        self.aboutLabel.setText(_translate("aboutDialog", "Nompy is a open-source calorie calculator written in Python. It uses PyQt Python binding for Qt framework version 5."))
        self.copyrightLabel.setText(_translate("aboutDialog", "<html><head/><body><p>© 2015 - <a href=\"http://lenarcic.eu/blog/\"><span style=\" text-decoration: underline; color:#0000ff;\">Istok Lenarčič</span></a></p></body></html>"))
        self.licenseLabel.setText(_translate("aboutDialog", "<html><head/><body><p>Licensed under <a href=\"http://www.gnu.org/licenses/gpl-3.0.en.html\"><span style=\" text-decoration: underline; color:#0000ff;\">GNU GPLv3 license</span></a>.</p></body></html>"))
        self.closeButton.setText(_translate("aboutDialog", "Close"))

