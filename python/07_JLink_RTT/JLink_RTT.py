# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import ctypes,  struct
import os, configparser,  time,  threading
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5 import  QtWidgets,  QtCore
from Ui_JLink_RTT import Ui_MainWindow

class SeggerRttBuf(object):
    def __init__(self, arr):
        self.sName,  self.pBuffer,  self.SizeOfBuffer,  self.WrOff,  self.RdOff,  self.Flags = arr
        
class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    received = QtCore.pyqtSignal(str)
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        self.connect_flag = False
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.initSetting()
        self.received.connect(self.textBrowser_view)
        threading.Thread(target=self.jlink_read).start()
        
        
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
    def upBuff0Empty(self):
        self.RttAddr = 0x100104e4
        b_len = 168
        buf = ctypes.create_string_buffer(b_len)
        self.jlink.JLINKARM_ReadMem(self.RttAddr, b_len, buf)
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
        return (self.upBuff0.RdOff == self.upBuff0.WrOff)
        
    def upBuff0Read(self):
        if self.upBuff0.RdOff < self.upBuff0.WrOff:
            len = self.upBuff0.WrOff - self.upBuff0.RdOff
            str = ctypes.create_string_buffer(len)
            raddr = self.upBuff0.pBuffer + self.upBuff0.RdOff
            self.jlink.JLINKARM_ReadMem(raddr, len, str)
            self.upBuff0.RdOff += len
            pRdOff_len = struct.pack("L", self.upBuff0.RdOff)
            buf = ctypes.create_string_buffer(pRdOff_len)
            rdoff_addr = self.RttAddr + 16+4*2+4*4
            self.jlink.JLINKARM_WriteMem(rdoff_addr, 4, buf)
        else:
            len = self.upBuff0.SizeOfBuffer - self.upBuff0.RdOff + 1
            str = ctypes.create_string_buffer(len)
            raddr = self.upBuff0.pBuffer + self.upBuff0.RdOff
            self.jlink.JLINKARM_ReadMem(raddr, len, str)
            self.upBuff0.RdOff = 0;
            pRdOff_len = struct.pack("L", self.upBuff0.RdOff)
            buf = ctypes.create_string_buffer(pRdOff_len)
            rdoff_addr = self.RttAddr+16+4*2+4*4
            self.jlink.JLINKARM_WriteMem(rdoff_addr, 4, buf)
            print("s:", pRdOff_len)
            print("rdoff_addr:%x"%(rdoff_addr))
        return str.raw.decode("utf_8")
        
    def jlink_read(self):
        print("jlink_read")
        while True:
            while self.connect_flag == True:
                print("connect_flag:", self.connect_flag)
                if not self.upBuff0Empty():
                    self.received.emit(self.upBuff0Read())
                time.sleep(0.9)
        
    def textBrowser_view(self, str):
        self.textBrowser.append(str)
        #self.textBrowser.append(str.decode("utf_8"))  #ascii    
        
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
            #str = ctypes.c_wchar("device=CR600")
            #print("exe:", self.jlink.JLINK_ExecCommand(str))
            #self.jlink.JLINK_ExecCommand(b"device=CR600")
            #pbuf_len = struct.pack("12s", "device=CR600")
            #buf = ctypes.create_string_buffer(pbuf_len)
            #val = self.jlink.JLINK_ExecCommand(buf)
            #print("var:", val)
            print("isopen:", isopen)
            str = ctypes.create_string_buffer(4)
            self.jlink.JLINKARM_ReadMem(0x10000000, 4, str)
            self.connect_flag = True
              
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
