# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets, QtCore

from Ui_01_test import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_6_clicked(self):
        """
        Slot documentation goes here.
        button6的槽函数
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        _translate = QtCore.QCoreApplication.translate
        print ("hello")
        self.label_2.setText(_translate("MainWindow", "china"))
        
    @pyqtSlot(bool)
    def on_pushButton_6_clicked(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        # TODO: not implemented yet
        raise NotImplementedError
        
    @pyqtSlot()
    def on_pushButton_7_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        _translate = QtCore.QCoreApplication.translate
        self.lineEdit.setText(_translate("MainWindow", ""))
    
    @pyqtSlot()
    def on_pushButton_8_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print (self.lineEdit.text())



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
    

