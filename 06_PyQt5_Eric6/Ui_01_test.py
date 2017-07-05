# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\python_study\eric6_project\01_test\01_test.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setToolTipDuration(-1)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(520, 20, 61, 31))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(240, 500, 414, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(490, 60, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setLineWidth(1)
        self.label_2.setObjectName("label_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_6.setGeometry(QtCore.QRect(570, 130, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 220, 75, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_8.setGeometry(QtCore.QRect(170, 220, 75, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 231, 201))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.pushButton_3.clicked.connect(MainWindow.showMaximized)
        self.pushButton_4.clicked.connect(MainWindow.showMinimized)
        self.pushButton_2.clicked.connect(MainWindow.showNormal)
        self.pushButton.clicked.connect(MainWindow.close)
        self.pushButton_5.clicked.connect(self.label_2.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "你好"))
        self.pushButton_3.setText(_translate("MainWindow", "最大化"))
        self.pushButton_4.setText(_translate("MainWindow", "最小化"))
        self.pushButton_2.setText(_translate("MainWindow", "正常"))
        self.pushButton.setText(_translate("MainWindow", "关闭"))
        self.pushButton_5.setText(_translate("MainWindow", "清零"))
        self.label_2.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#0000ff;\">hhh</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "hello_world!"))
        self.pushButton_6.setText(_translate("MainWindow", "edit"))
        self.pushButton_7.setText(_translate("MainWindow", "清除"))
        self.pushButton_8.setText(_translate("MainWindow", "打印信息"))
        self.lineEdit.setText(_translate("MainWindow", "please input:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

