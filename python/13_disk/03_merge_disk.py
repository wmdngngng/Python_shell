import os
import wmi
import win32file
import pywintypes
import win32con
import struct

BIN_OUT     = "jiaxing_evb.bin"
SECTOR_SIZE = 512

BIN_FILES = [
["uboot_evb.img",           0],             #
["env.bin",                 2816],          #0x0B00@1.375M
["uImage",                  4096],          #0x1000@2M
["nextvpu_jiaxing_evb.dtb", 12288],         #0x3000@6M 
["DSP_v11.bin",             16384],         #0x4000@8M
["DSP_v11.bin",             20480],         #0x5000@10M  
["DSP_v11.bin",             24576],         #0x6000@12M  
["DSP_v11.bin",             28672],         #0x7000@14M  
["fs_ext4.img",             40960],         #0xA000@20M 
["rootfs.img",              43008],         #0xA800@21M  
]
a=[[1,2,3],[4,5,6]]
def merge():
    for bin_file in BIN_FILES:
        if False == os.path.exists(bin_file[0]):
            exit(bin_file[0]+" is not exist!")
            
    print("Creat "+BIN_OUT)
    offset = 0
    index = 0
    if os.path.exists(BIN_OUT):
        os.remove(BIN_OUT)
    
    file_out = open(BIN_OUT, 'ab')
    value = struct.pack('B', 0x00)
    
    for bin_file in BIN_FILES:
        if index > 0:
            file = open(BIN_FILES[index-1][0], 'rb')
            data = file.read()
            file_out.write(data)
            offset = file_out.tell()
            file.close()
            print(index,BIN_FILES[index-1][0],offset,SECTOR_SIZE*bin_file[1])
            while offset < (SECTOR_SIZE*bin_file[1]):
                file_out.write(value)
                offset = file_out.tell()
        index = index + 1
    file = open(BIN_FILES[index-1][0], 'rb')
    data = file.read()
    file_out.write(data)
    offset = file_out.tell()
    file.close()
    print(index,BIN_FILES[index-1][0],"%dB=%dKB=%dMB"%(offset,offset/1024,offset/1024/1024))
    print("sector:%f"%(offset/512))
    
def get_removable_disk():
    index = 0
    disks_list = []
    c = wmi.WMI()
    for disk in c.Win32_DiskDrive():
        if disk.MediaType == "Removable Media":
            tempdisk = {}
            index = index + 1
            print("Index=%d Disk=%d" %(index, disk.Index), disk.InterfaceType,
                "%5.1fG" %(int(disk.Size)/1000/1000/1000))
            tempdisk["index"] = index
            tempdisk["disk"] = disk.Index
            tempdisk["ID"] = disk.DeviceID
            disks_list.append(tempdisk)
    if index > 1:
        sel_index = input("Please Input Index:")
    elif index == 1:
        sel_index = index
    else:
        exit("\r\nERROR:SD not found!")
    
    for disk_list in disks_list:
        if disk_list["index"] == int(sel_index):
            print("select index=%d"%(index))
            disk_name = disk_list["ID"][4:]
            hfile=win32file.CreateFile("\\\\.\\"+disk_name, win32con.GENERIC_WRITE, 0,None, win32con.OPEN_EXISTING, 0 , None)
            file = open(BIN_OUT,'rb')
            data = file.read()
            win32file.WriteFile(hfile, data)
            hfile.Close()
            print("\r\nSUCCESS: SD write finash!")
            
if __name__ == '__main__':
    merge()
    #get_removable_disk()