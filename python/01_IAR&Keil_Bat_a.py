# 说明：修改文件内容，为 IAR 工程合并前做处理
# 1. 在.py当前目录下的每一个工程文件夹下创建IAR和Keil文件夹
# 2. 检查icf文件的名字，将首字母为C的改为c
# 3. copy 当前目录下的每一个工程文件夹下的ewd,eww,ewt,ewp,icf文件到IAR目录下
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

CurrDir = os.getcwd()

Ref_Dir_F = "Ref_Dir"
Exclude_F1 = "协议栈demo基本连接关系图"
Exclude_F2 = "协议栈demo实物连接图"
Exclude_F3 = "demo1_plc"

def CreateDir(path):
    os.mkdir(os.path.join(path,"IAR"))
    os.mkdir(os.path.join(path,"Keil"))

def Move2file(path):
    for dir_name in os.listdir(path):
        print ("2:"+dir_name)
        Srcfile = os.path.join(path , dir_name)
        Dstfile = os.path.join(path , "IAR")          
        if dir_name[-4:] == d_ewp:          
            shutil.move(Srcfile,Dstfile)
        elif dir_name[-4:] == d_eww:
            shutil.move(Srcfile,Dstfile)
        elif dir_name[-4:] == d_ewt:
            shutil.move(Srcfile,Dstfile)
        elif dir_name[-4:] == d_ewd:
            shutil.move(Srcfile,Dstfile)
        elif dir_name[-4:] == d_icf:
            shutil.move(Srcfile,Dstfile)

def RenameIcf(path):
    for dir_name in os.listdir(path):
        print ("2:"+dir_name)
        if dir_name[-4:] == d_icf:
            if dir_name[0] == "C":
                new_name = "c"+dir_name[1:]
                src_rename = os.path.join(path,dir_name)
                dst_rename = os.path.join(path,new_name)
                os.rename(src_rename,dst_rename)
        
    
def main():
    for dir_name in os.listdir(CurrDir):
        if not ((dir_name == Ref_Dir_F)or(dir_name == Exclude_F1)or(dir_name == Exclude_F2)or(dir_name == Exclude_F3)):
            if os.path.isdir(dir_name):
                NextDir = os.path.join(CurrDir , dir_name)
                print ("1:"+NextDir)
                CreateDir(NextDir)
                RenameIcf(NextDir)
                Move2file(NextDir)
            

'''
def main():
    for parent, dir_names, file_names in os.walk(CurrDir):
        for dir_name in dir_names:
            NextDir = parent + dir_name
            print ("Dir:" + NextDir)
            if NextDir == os.getcwd():
                #print ("Dir:" + os.getcwd()) #print ("parent:" + parent+dir_name)
                print ("Dir:" + NextDir)
                #CreatePrj()
'''

if __name__ == "__main__":
    main()