# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import ctypes,  struct
import os, configparser
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
        self.initSetting()
        
    def initSetting(self):
        self.settingPath = "../setting.ini"
        if os.path.exists(self.settingPath):
            self.conf = configparser.ConfigParser()
            self.conf.read(self.settingPath)
            self.dllPath = self.conf.get("globals", "Dll_Path")
            self.mapPath = self.conf.get("globals", "Map_Path")
            self.lineEdit_dll.setText(self.dllPath)
            self.lineEdit_map.setText(self.mapPath)
                
        else:
            self.textBrowser("Error:setting.ini not found.")
        
    @pyqtSlot()
    def on_toolButton_jlink_lj_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.tempPath, filetype = QFileDialog.getOpenFileName(self, "jLink_ARM.dll Path", "D:",  "*.dll" )
        if (len(self.tempPath)):
            self.dllPath = self.tempPath
            self.lineEdit_dll.setText(self.dllPath)
            print(self.dllPath)
        
    
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
        self.textBrowser.append(self.dllPath)
        try:
            self.jlink = ctypes.cdll.LoadLibrary(self.dllPath)
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
        self.jlink.JLINKARM_Close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
