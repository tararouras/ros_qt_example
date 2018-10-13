# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/example.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        StackedWidget.setObjectName("StackedWidget")
        StackedWidget.resize(400, 300)
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.goButton = QtWidgets.QPushButton(self.page1)
        self.goButton.setObjectName("goButton")
        self.gridLayout.addWidget(self.goButton, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        StackedWidget.addWidget(self.page1)
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.waitingLabel = QtWidgets.QLabel(self.page2)
        self.waitingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.waitingLabel.setObjectName("waitingLabel")
        self.gridLayout_3.addWidget(self.waitingLabel, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        StackedWidget.addWidget(self.page2)

        self.retranslateUi(StackedWidget)
        QtCore.QMetaObject.connectSlotsByName(StackedWidget)

    def retranslateUi(self, StackedWidget):
        _translate = QtCore.QCoreApplication.translate
        StackedWidget.setWindowTitle(_translate("StackedWidget", "StackedWidget"))
        self.goButton.setText(_translate("StackedWidget", "Go"))
        self.waitingLabel.setText(_translate("StackedWidget", "Waiting.."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StackedWidget = QtWidgets.QStackedWidget()
    ui = Ui_StackedWidget()
    ui.setupUi(StackedWidget)
    StackedWidget.show()
    sys.exit(app.exec_())

