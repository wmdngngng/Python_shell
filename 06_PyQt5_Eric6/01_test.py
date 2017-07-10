# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QInputDialog, QLineEdit, QFileDialog  
from PyQt5 import QtWidgets, QtCore
from zdy_dialog import dialog

from Ui_01_test import Ui_MainWindow
import webbrowser

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
        self.graphicsView.mousePressEvent = self.graphicsView_Click
        
    def graphicsView_Click(self, gevent):
        print("你点击了图片")
        webbrowser.open("www.baidu.com")
    
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
    
    @pyqtSlot()
    def on_pushButton_gy_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        QMessageBox.about(self, "About",  "关于内容\r\n没有返回值")
    
    @pyqtSlot()
    def on_pushButton_tz_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        QMessageBox.information(self, "Information", "通知内容")
    
    @pyqtSlot()
    def on_pushButton_jg_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        QMessageBox.warning(self, "Warning",  "警告内容\r\n第五个参数是默认值", QMessageBox.Reset|QMessageBox.Help|QMessageBox.Cancel|QMessageBox.Yes, QMessageBox.Reset)
    
    @pyqtSlot()
    def on_pushButton_xw_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        xw_button = QMessageBox.question(self, "Question", "询问内容", QMessageBox.Ok|QMessageBox.No)
        if xw_button==QMessageBox.Ok:
            self.textBrowser.append("你点击了 Ok")
        elif xw_button == QMessageBox.No:
            self.textBrowser.append("你点击了 No")
    
    @pyqtSlot()
    def on_pushButton_ab_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        QMessageBox.aboutQt(self, "AboutQT") #no return
    
    @pyqtSlot()
    def on_pushButton_yz_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        QMessageBox.critical(self, "Error",  "严重警告内容\r\n默认返回QMessageBox.Ok")

    @pyqtSlot()
    def on_pushButton_zfc_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        zfc_str, ok = QInputDialog.getText(self,  "字符串", "请在此输入：", QLineEdit.Normal, "Please input:")
        print(zfc_str,  ok)
        if ok and (len(zfc_str) != 0):
            self.textBrowser.append(zfc_str)
        
    @pyqtSlot()
    def on_pushButton_zx_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        input_str, ok = QInputDialog.getInt(self,  "整形输入", "请在此输入：", 27, 1, 0, 120)
        print(input_str,  ok)
    
    @pyqtSlot()
    def on_pushButton_fd_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        input_str, ok = QInputDialog.getDouble(self,  "浮点输入", "请在此输入：", 27.1, -1000, 1200)
        print(input_str,  ok)
    
    @pyqtSlot()
    def on_pushButton_xlk_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        xlk_list = ["CPU", "显示器", "键盘", "鼠标"]
        xlk_str, ok = QInputDialog.getItem(self, "下拉框", "请输入", xlk_list)
        print (xlk_str, ok)
        if ok:
            self.textBrowser.append(xlk_str)
        

    @pyqtSlot()
    def on_pushButton_11_zdy_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        zdy_dialog = dialog()
        zdy_dialog.exec_()
#*************************************************************************
#*********************  Action  *******************************************
#*************************************************************************
    @pyqtSlot()
    def on_actionopen_triggered(self):
        """
        Slot documentation goes here.
        """
        print("你点击了 open")
        file_path_str, filetype  = QFileDialog.getOpenFileName(self, "打开文件", "/", "*.txt;;*")
        print(file_path_str)
        print(filetype)
        if len(file_path_str):
            f = open(file_path_str)
            data_str = f.read()
            f.close
            self.textBrowser.append(data_str)
    
    @pyqtSlot()
    def on_actionclose_triggered(self):
        """
        Slot documentation goes here.
        """
        print("你点击了 close")
    
    @pyqtSlot()
    def on_actionsave_triggered(self):
        """
        Slot documentation goes here.
        """
        print("你点击了 save")
        save_data_path, filetype = QFileDialog.getSaveFileName(self, "保存文件", "/", "*.txt;;*")
        print(save_data_path)
        print(filetype)
        get_data = self.textBrowser.toPlainText()
        f = open(save_data_path, "a+")
        f.write(get_data)
        f.close()
    
    @pyqtSlot()
    def on_actionexit_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        sys.exit(0)
    
    @pyqtSlot()
    def on_actioncopy_triggered(self):
        """
        Slot documentation goes here.
        """
        print("你点击了 copy")
    
    @pyqtSlot()
    def on_actioncut_triggered(self):
        """
        Slot documentation goes here.
        """
        print("你点击了 cut")
    
    @pyqtSlot()
    def on_actionpaset_triggered(self):
        """
        Slot documentation goes here.
        """
        print("你点击了 paset")
    
    @pyqtSlot()
    def on_actionmax_triggered(self):
        """
        Slot documentation goes here.
        """
        print("你点击了 max")
    
    @pyqtSlot()
    def on_actionmin_triggered(self):
        """
        Slot documentation goes here.
        """
        print("你点击了 min")
    
    @pyqtSlot()
    def on_actionabout_triggered(self):
        """
        Slot documentation goes here.
        """
        QMessageBox.about(self, "Version",  "此软件是学习Python而作,仅供参考。\r\nVersion:1.0.0\r\nTime:2017/07/09")
    
    @pyqtSlot()
    def on_actionabout_auther_triggered(self):
        """
        Slot documentation goes here.
        """
        QMessageBox.information(self, "关于作者", "Labc")
    
    @pyqtSlot()
    def on_actionhelp_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print("你点击了 help")
    
    @pyqtSlot()
    def on_actionconnect_us_triggered(self):
        """
        Slot documentation goes here.
        """
        print("你点击了 connect us")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
    
