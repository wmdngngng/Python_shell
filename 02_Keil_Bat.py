# 说明：修改文件内容，Keil 工程合并批处理
# 1. 排除不需要处理的文件
# 2. 判断Keil文件夹是否存在，将模板文件copy到存在的Keil文件夹里
# 3. 存储每个目标文件夹下CustomProject.xml里的信息
# 4. 存储每个目标文件夹下*.uvprojx里的信息
# 5. 将两个存储的信息对比，保存相同信息
# 6. 先处理相同信息的部分，在处理不同信息的部分
#
# @Author: labc
# Created on June 21 2017
#
#

import os
import shutil
import xml.dom.minidom as minidom
from collections import defaultdict
from xml.etree.ElementTree import ElementTree,Element

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

D_uvprojx = ".uvprojx"
D_uvoptx = ".uvoptx"
Ref_tx_file = "Ref_Dir.uvoptx"
Ref_jx_file = "Ref_Dir.uvprojx"
Des_file = "CustomProject.xml"
Ini_file = "JLinkSettings.ini"
Jscript_file = "ClouderSemi_CR600.JLinkScript"

Keil_F = "Keil"
Exclude_F1 = "协议栈demo基本连接关系图"
Exclude_F2 = "协议栈demo实物连接图"
Ref_Dir_F = "Ref_Dir"

CurrDir = os.getcwd()
Uvoptx_Dir = os.path.join(CurrDir,Ref_Dir_F,Keil_F,Ref_tx_file)
Uvprojx_Dir = os.path.join(CurrDir,Ref_Dir_F,Keil_F,Ref_jx_file)
Ini_Dir = os.path.join(CurrDir,Ref_Dir_F,Keil_F,Ini_file)
Jscript_Dir = os.path.join(CurrDir,Ref_Dir_F,Keil_F,Jscript_file)

def Add_Content(files_elem, content):
    'add content in uvoptx'
    file_elem = Element("File")
    file_name_elem = Element("FileName")
    file_type_elem = Element("FileType")
    file_path_elem = Element("FilePath")
    files_elem.append(file_elem)
    file_elem.append(file_name_elem)
    file_elem.append(file_type_elem)
    file_elem.append(file_path_elem)
    filename_text = content[content.rfind("\\")+1:]
    
    if filename_text.endswith(".c"):
        file_type_elem.text = "1"
    elif filename_text.endswith(".s"):
        file_type_elem.text = "2"
    elif filename_text.endswith(".a"):
        filename_text = filename_text.replace(".a", ".lib")  
        content = content.replace(".a", ".lib")
        print ("15:",filename_text,content)
        file_type_elem.text = "4"
    elif filename_text.endswith(".lib"):
        file_type_elem.text = "4"    
    elif filename_text.endswith(".h"):
        file_type_elem.text = "5"
    
    file_name_elem.text = filename_text    
    file_path_elem.text = content[11:]
    
def CreatedNode(root,groupname,content,flag_bool):
    flag = 0
    gfile_s = []
    elem_group = Element("Group")
    elem_groupname = Element("GroupName")
    elem_files = Element("Files")
    
    if len(content) == 0:
        return
    #print ("13:"+content)
    if flag_bool == 1:  #have the "GroupName"
        for child in root:
            for group in child.iter("Group"):
                for gname in group.iter("GroupName"):
                    if gname.text == groupname:
                        flag = 1
                        break
                if flag == 1: #need add content in groupname
                    for group_elem in group:
                        print ("14: "+group_elem.tag)
                        if group_elem.tag == "Files":  #have the "Files"
                            Add_Content(group_elem, content)
                            break
                    else:
                        group.append(elem_files)  #have no "Files"
                        Add_Content(elem_files, content)
                    flag = 0
    elif flag_bool == 2:  #have no the "GroupName"
        for child in root:
            for groups in child.iter("Groups"):
                groups.append(elem_group)
                elem_group.append(elem_groupname)
                elem_group.append(elem_files)
                elem_groupname.text = groupname
                for cont in content:
                    Add_Content(elem_files, cont)


def Find_FilePath(gname, gfile=[]):
    fpaths=[]
    fnames=[]
    flag_t = 0
    index_flag = 0
    for filepath in gfile:
        if gname == filepath:
            flag_t = 1
            index_flag = gfile.index(filepath)
            
        if flag_t == 1:
            if not gfile.index(filepath) == index_flag:
                if filepath[:10] == "$PROJ_DIR$":
                    fpaths.append(filepath)
                    start = filepath.rfind("\\");
                    fnames.append(filepath[start+1:])
                    print("11:"+filepath, filepath[start+1:])
                else:
                    return fpaths
    return fpaths

def Edit_Uvprojx(path, file):
    CcDefines=[]
    CcIncludePath2=[]
    GroupFiles=[]
    gnames = []
    gname_same = []
    gname_diff = []
    files_path = []
    
    xml_dir = os.path.join(path,Des_file)
    if not os.path.exists(xml_dir):
        print ("**************************\r\n")
        print (Des_file+" folder is not existence")
        return
    xml_tree = ET.parse(xml_dir)
    xml_root = xml_tree.getroot()
    for child in xml_root:
        if (child.tag == "CCDefines"):
            CcDefines.append(child.text)
        elif (child.tag == "CCIncludePath2"):
            CcIncludePath2.append(child.text)
        elif (child.tag == "group"):
            for gname in child.iter("name"):
                GroupFiles.append(gname.text) 
            for gfile in child.iter("file"):
                GroupFiles.append(gfile.text)

    for defines in CcDefines:
        print ("1: "+defines) 
    for path2 in CcIncludePath2:
        print ("2: "+path2)
    for pname in GroupFiles:
        print ("3: "+pname)
    print ("4:")

    uvprojx_dir = os.path.join(path,Keil_F,file+D_uvprojx)
    uvprojx_tree = ET.parse(uvprojx_dir)
    uvprojx_root = uvprojx_tree.getroot()

    for child in uvprojx_root:
        for deins in child.iter("Cads"):  #seach tag=Cads
            for de in deins.iter("Define"): #edit Define string
                de_strings = de.text
                print (de_strings)
                for cfile in CcDefines:
                    print ("5:"+cfile)
                    de_strings = de_strings + " " + cfile
                    print (de_strings)
                de.text = de_strings
            for ins in deins.iter("IncludePath"): #edit IncludePath string
                ins_strings = ins.text
                #print ("6: "+ins_strings)
                for ifile in CcIncludePath2:
                    print ("6.1: "+ifile)
                    ins_strings = ins_strings+";"+ifile[11:]
                    #print ("6.2: "+ins_strings)
                ins.text = ins_strings

    for child in uvprojx_root:
        for groupss in child.iter("Groups"):
            for gname in groupss.iter("GroupName"):
                gname_text = gname.text
                print ("7.1: ",gname_text)
                gnames.append(gname_text)

    for gfile in GroupFiles:
        for gname in gnames:
            if gfile == gname:
                print ("7.2: ",gfile)
                gname_same.append(gname)
                break
        else:
            #print ("7.3: ",gfile)
            if not gfile[:10]=="$PROJ_DIR$":
                print ("7.4: ",gfile)
                gname_diff.append(gfile)

    for file_s in gname_same:
        print ("8.1: ",file_s)
        for file in Find_FilePath(file_s, GroupFiles):
            print ("8.2:",file)
            CreatedNode(uvprojx_root, file_s, file,1)
            
    for file_d in gname_diff:        
        print ("8.3:",file_d)
        files_path = []
        for file in Find_FilePath(file_d, GroupFiles):
            print ("8.4:",file)
            files_path.append(file)
        CreatedNode(uvprojx_root, file_d, files_path,2)
            
    uvprojx_tree.write(uvprojx_dir,encoding='UTF-8',xml_declaration=True )   

def Edit_Uvprojx_SDK(path, file):
    'The function is add the xxx_sdk.uvoptx and xxx_sdk.uvprojx'
    keil_dir = os.path.join(path, Keil_F)
    if os.path.exists(keil_dir):
        file_tx_dir = os.path.join(keil_dir,file+D_uvoptx);
        file_jx_dir = os.path.join(keil_dir,file+D_uvprojx);
        shutil.copyfile(file_tx_dir, keil_dir+"\\"+file+"_SDK"+D_uvoptx)
        shutil.copyfile(file_jx_dir, keil_dir+"\\"+file+"_SDK"+D_uvprojx)
        
        sdk_uvprojx_dir = os.path.join(keil_dir,file+"_SDK"+D_uvprojx)
        sdk_uvprojx_tree = ET.parse(sdk_uvprojx_dir)
        sdk_uvprojx_root = sdk_uvprojx_tree.getroot()
        for child in sdk_uvprojx_root:
            for groups in child.iter("Groups"):  #seach the label "Groups"
                for group in groups.iter("Group"):
                    for groupname in group.iter("GroupName"):  #seach the label "GroupName"
                        if groupname.text == "cr600_driver":
                            for files in group.iter("Files"):
                                for file in files:
                                    for file_type in file:
                                        print("17",file_type.text)
                                        file.remove(file_type)
        
    
def Clear_file(path,files):
    print ("Clear_file: "+path)
    keil_dir = os.path.join(path, Keil_F)
    if os.path.exists(keil_dir):
        print ("Clear_file1: "+keil_dir)
        shutil.rmtree(keil_dir)  #remove Keil folder
    else:
        print (Keil_F+" folder is not existence")
    for file in os.listdir(path):
        if file == Des_file:
            os.mkdir(keil_dir)  #add Keil folder
            #add .ini and .jlinkscript in Keil folder
            shutil.copyfile(Ini_Dir,keil_dir+"\\"+Ini_file)
            shutil.copyfile(Jscript_Dir,keil_dir+"\\"+Jscript_file)
            shutil.copyfile(Uvoptx_Dir,keil_dir+"\\"+files+D_uvoptx)
            shutil.copyfile(Uvprojx_Dir,keil_dir+"\\"+files+D_uvprojx)
            
def main():
    for file1 in os.listdir(CurrDir):
        #if ((file1 == "03_ADC")or(file1=="02_DAC")or(file1=="QQ_IOT_DEMO")):
        file2_dir = os.path.join(CurrDir,file1)
        if not ((Exclude_F1== file1)or(Exclude_F2== file1)or(Ref_Dir_F==file1)):
            if os.path.isdir(file1):
                print ("main: "+file1)   
                Clear_file(file2_dir,file1)
                Edit_Uvprojx(file2_dir, file1) #cd Keil floder
                Edit_Uvprojx_SDK(file2_dir, file1)
 
if __name__ == "__main__":
    main()