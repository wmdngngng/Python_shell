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
        #print (self.lineEdit.text())
        input_string = self.lineEdit.text()
        self.textBrowser.append(input_string)

    @pyqtSlot()
    def on_pushButton_9_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        b9_string = self.textBrowser.toPlainText()
        print(b9_string)
    
    @pyqtSlot()
    def on_pushButton_10_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.textBrowser.clear()

    @pyqtSlot()
    def on_radioButton_ty_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        ty_string = "你选择了同意"
        print(ty_string)
        self.textBrowser.append(ty_string)
        self.radioButton_jb.setChecked(True)
    
    @pyqtSlot()
    def on_radioButton_bty_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        bty_string = "你选择了不同意"
        print(bty_string)
        self.textBrowser.append(bty_string)
        self.radioButton_bjb.setChecked(True)
        
    @pyqtSlot()
    def on_radioButton_jb_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        jb_string = "你选择了加班"
        print(jb_string)
        self.textBrowser.append(jb_string)
    
    @pyqtSlot()
    def on_radioButton_bjb_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        bjb_string = "你选择了不加班"
        print(bjb_string)
        self.textBrowser.append(bjb_string)

    @pyqtSlot(int)
    def on_dial_valueChanged(self, value):
        """
        Slot documentation goes here.
        
        @param value DESCRIPTION
        @type int
        """
        # TODO: not implemented yet
        #self.textBrowser.append(self, str=value)
        print(value)
        self.lcdNumber.display(value*10.3)
        print(value*10.3)
        self.horizontalSlider.setValue(value)
        self.verticalSlider.setValue(value)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
    
