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

class SeggerRttBuf(object):
    def __init__(self, arr):
        self.sName,  self.pBuffer,  self.SizeOfBuffer,  self.WrOff,  self.RdOff,  self.Flags = arr
        
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
            isopen = self.jlink.JLINKARM_IsOpen()
            print("123:")
            #str = "device=CR600"
            #str = ctypes.c_wchar_p("device=CR600")
            #print("exe:", self.jlink.JLINK_ExecCommand(ctypes.c_char_p("device=CR600")))
            print("isopen:", isopen)
            RttAddr = 0x100104e4
            b_len = 168
            buf = ctypes.create_string_buffer(b_len)
            self.jlink.JLINKARM_ReadMem(RttAddr, b_len, buf)
            acID, MaxNumUpBuf, MaxNumDownBuf = struct.unpack("16sii", buf.raw[:24])
            upBuffEnd = 24+24*1
            downBuffStart = 24+24*MaxNumUpBuf
            downBuffEnd = downBuffStart+24
            upBuffs0 = struct.unpack("PPiiii", buf.raw[24:upBuffEnd])
            downBuffs0 = struct.unpack("PPiiii", buf.raw[downBuffStart:downBuffEnd])
            self.upBuff0 = SeggerRttBuf(upBuffs0)
            self.downBuff0 = SeggerRttBuf(downBuffs0)
            print("sName:%x"%(self.upBuff0.sName))
            print("pBuffer:%x"%(self.upBuff0.pBuffer))
            print("SizeOfBuffer:%d"%(self.upBuff0.SizeOfBuffer))
            print("WrOff:%d"%(self.upBuff0.WrOff))
            print("RdOff:%d"%(self.upBuff0.RdOff))
            print("Flags:%d"%(self.upBuff0.Flags))
            
            if self.upBuff0.RdOff < self.upBuff0.WrOff:
                len = self.upBuff0.WrOff - self.upBuff0.RdOff
                str = ctypes.create_string_buffer(len)
                raddr = self.upBuff0.pBuffer + self.upBuff0.RdOff
                self.jlink.JLINKARM_ReadMem(raddr, len, str)
                self.upBuff0.RdOff += len
                pRdOff_len = struct.pack("L", self.upBuff0.RdOff)
                buf = ctypes.create_string_buffer(pRdOff_len)
                rdoff_addr = RttAddr + 16+4*2+4*4
                self.jlink.JLINKARM_WriteMem(rdoff_addr, 4, buf)
                
            else:
                len = self.upBuff0.SizeOfBuffer - self.upBuff0.RdOff + 1
                str = ctypes.create_string_buffer(len)
                raddr = self.upBuff0.pBuffer + self.upBuff0.RdOff
                self.jlink.JLINKARM_ReadMem(raddr, len, str)
                self.upBuff0.RdOff = 0;
                pRdOff_len = struct.pack("L", self.upBuff0.RdOff)
                buf = ctypes.create_string_buffer(pRdOff_len)
                rdoff_addr = RttAddr+16+4*2+4*4
                self.jlink.JLINKARM_WriteMem(rdoff_addr, 4, buf)
                print("ebuf:", buf)
                print("s:", pRdOff_len)
                print("rdoff_addr:%x"%(rdoff_addr))
             
            print("str:", str)
            print("str.raw:", str.raw)
            print("str.value:", str.value)
            real_str = str.raw.decode("utf_8")
            self.textBrowser.append("hello")
            self.textBrowser.append(str.raw.decode("utf_8"))  #ascii
              
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
