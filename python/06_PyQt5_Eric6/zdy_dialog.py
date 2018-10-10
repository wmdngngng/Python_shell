# -*- coding: utf-8 -*-

"""
Module implementing dialog.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QInputDialog

from Ui_zdy_dialog import Ui_dialog


class dialog(QDialog, Ui_dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(dialog, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_tj_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        tj_str = self.lineEdit_xm.text()
        tj_dh_str = self.lineEdit_9dh.text()
        print("你输入的姓名是：", tj_str)
        print("你输入的电话是：", tj_dh_str)
        self.close()
    
    @pyqtSlot()
    def on_pushButton_2cz_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print("你点击了重置")
    
    @pyqtSlot()
    def on_radioButton_2boy_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print("你选择了男性")
    
    @pyqtSlot()
    def on_radioButton_1girl_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print("你选择了女性")
    
    @pyqtSlot()
    def on_toolButton_2nl_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        nl_int, ok = QInputDialog.getInt(self,  "年龄", "请在此输入：", 0, 18, 0, 120)
        print(nl_int, ok)
        if ok:
            print("你输入的年龄是：", nl_int)
    
    @pyqtSlot()
    def on_toolButton_sg_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        sg_dou, ok = QInputDialog.getDouble(self, "身高", "请在此输入：", 0, 50.0, 0, 600)
        print(sg_dou, ok)
        if ok:
            print("你输入的身高是：", sg_dou)
