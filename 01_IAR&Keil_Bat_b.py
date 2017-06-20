# 说明：修改文件内容，为 IAR 工程合并前做处理
# 1. 除 “Ref_Dir”，“协议栈demo基本连接关系图”，“协议栈demo实物连接图”，“demo1_plc”
#    四个文件夹不处理，其他文件夹均做如下处理
# 2. 将每个 xml 文件里的 "$PROJ_DIR$" 替换为 "$PROJ_DIR$\.."
#
# @Author: labc
# Created on June 20 2017
#
#

import os
import shutil

d_ewp = ".ewp" 
d_eww = ".eww"
d_ewt = ".ewt"
d_ewd = ".ewd"
d_icf = ".icf"
d_xml = ".xml"

oldstr = "$PROJ_DIR$"
newstr = "$PROJ_DIR$\.."
Ref_Dir_F = "Ref_Dir"
Exclude_F1 = "协议栈demo基本连接关系图"
Exclude_F2 = "协议栈demo实物连接图"
Exclude_F3 = "demo1_plc"

CurrDir = os.getcwd()

def handle_xml(path):
    for file in os.listdir(path):
        if file[-4:] == d_xml:       #find the xml file
            file_dir = os.path.join(path,file)
            print ("2:"+file_dir)
            file_xml = open(file_dir,"r+")
            file_xmls = file_xml.readlines()
            file_xml.seek(0)
            file_xml.truncate()
            for line_xml in file_xmls:
                #if line_xml.find(oldstr) >= 0:
                line_xml = line_xml.replace(oldstr,newstr)
                file_xml.write(line_xml)            
            file_xml.close()

def main():
    for dir_name in os.listdir(CurrDir):
        if not ((dir_name == Ref_Dir_F)or(dir_name == Exclude_F1)or(dir_name == Exclude_F2)or(dir_name == Exclude_F3)):
            if os.path.isdir(dir_name):
                file_dir1 = os.path.join(CurrDir , dir_name)
                print ("file_dir1: "+file_dir1)
                handle_xml(file_dir1)

if __name__ == "__main__":
    main()