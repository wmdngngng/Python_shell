# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\python_study\Python_Study\07_JLink_RTT\JLink_RTT.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser.setGeometry(QtCore.QRect(70, 60, 501, 381))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(60, 480, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(60, 510, 111, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_jlink = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_jlink.setGeometry(QtCore.QRect(170, 480, 351, 20))
        self.lineEdit_jlink.setObjectName("lineEdit_jlink")
        self.lineEdit_map = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_map.setGeometry(QtCore.QRect(170, 510, 351, 20))
        self.lineEdit_map.setObjectName("lineEdit_map")
        self.toolButton_jlink_lj = QtWidgets.QToolButton(self.centralWidget)
        self.toolButton_jlink_lj.setGeometry(QtCore.QRect(530, 480, 37, 18))
        self.toolButton_jlink_lj.setObjectName("toolButton_jlink_lj")
        self.toolButton_map_lj = QtWidgets.QToolButton(self.centralWidget)
        self.toolButton_map_lj.setGeometry(QtCore.QRect(530, 510, 37, 18))
        self.toolButton_map_lj.setObjectName("toolButton_map_lj")
        self.pushButton_connect = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_connect.setGeometry(QtCore.QRect(490, 560, 75, 23))
        self.pushButton_connect.setObjectName("pushButton_connect")
        self.pushButton_clear = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(60, 560, 75, 23))
        self.pushButton_clear.setObjectName("pushButton_clear")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Jlink_ARM.dll路径："))
        self.label_2.setText(_translate("MainWindow", "项目.map文件路径："))
        self.toolButton_jlink_lj.setText(_translate("MainWindow", "..."))
        self.toolButton_map_lj.setText(_translate("MainWindow", "..."))
        self.pushButton_connect.setText(_translate("MainWindow", "Connect"))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear"))

'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
'''
