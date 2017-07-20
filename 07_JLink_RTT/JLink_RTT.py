# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import ctypes,  struct
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5 import  QtWidgets
from Ui_JLink_RTT import Ui_MainWindow


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
    def on_toolButton_jlink_lj_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.jlinkPath, filetype = QFileDialog.getOpenFileName(self, "jLink_ARM.dll Path", "D:",  "*.dll" )
        print(self.jlinkPath)
        self.lineEdit_jlink.setText(self.jlinkPath)
        
    
    @pyqtSlot()
    def on_toolButton_map_lj_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        mapPath,  filetype = QFileDialog.getOpenFileName(self, "Map File Path", "/", "*map")
        self.lineEdit_map.setText(mapPath)
    
    @pyqtSlot()
    def on_pushButton_connect_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.textBrowser.append("Conneting...")
        self.textBrowser.append(self.jlinkPath)
        try:
            self.jlink = ctypes.cdll.LoadLibrary(self.jlinkPath)
            self.jlink.JLINKARM_TIF_Select(1)
            sel_device = self.jlink.JLINKARM_GetSelDevice()
            print("sel device:", sel_device)
        except Exception as ex:
                print (ex)
        else:
            print("关闭连接")
            isopen = self.jlink.JLINKARM_IsOpen()
            print("isopen:", isopen)
            buf = ctypes.create_string_buffer(10)
            self.jlink.JLINKARM_ReadMem(0x10000000, 10, buf)
            print("buf:", buf.raw)
    
    @pyqtSlot()
    def on_pushButton_clear_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.textBrowser.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
