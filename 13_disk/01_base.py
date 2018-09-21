import os
import wmi
import win32file
import pywintypes
import win32con


def get_disk_info():
    """
    :return: get the disk info
    """
    tmplist = []
    c = wmi.WMI()
    for physical_disk in c.Win32_DiskDrive():
        tmpdict ={}
        #tmpdict["FreeSpace"] = physical_disk.Signature
        tmpdict["Caption"] = physical_disk.Caption
        tmpdict["Size"] = int(physical_disk.Size)/1024/1024/1024
        tmplist.append(tmpdict)
    return tmplist
    
def get_logic_info():
    #templist = []
    c = wmi.WMI()
    for logic in c.Win32_LogicalDisk():
        if logic.Size != None:
            print("01",logic.Caption)    #打印盘符
            print("02",int(logic.Size)/1024/1024/1024)
            print("10",logic.Description)
            print("12",logic.DeviceID)
            print("12",logic.DriveType)
            print("13",logic.FileSystem)
            print("17",logic.MediaType)
            print("35",logic.VolumeName)
            print("\n")
    #tmpdict["xxx"] = 
    #templist.append(tmpdict)
    

def get_removable_disk():
    c = wmi.WMI()
    for disk in c.Win32_LogicalDisk():
        if disk.DriveType == 2:     #removable
            print(disk.Caption,disk.Size)
            print("12",disk.NumberOfBlocks)
            #print("%4.1f" %(int(disk.Size)/1024/1024/1024))
            #hfile=win32file.CreateFile("\\\\.\\PhysicalDrive2"+disk.Caption, win32con.GENERIC_READ|win32con.GENERIC_WRITE,
            hfile=win32file.CreateFile("\\\\.\\PHYSICALDRIVE2", win32con.GENERIC_READ|win32con.GENERIC_WRITE,
                win32con.FILE_SHARE_READ|win32con.FILE_SHARE_WRITE,
                None, win32con.OPEN_EXISTING, 0 , None)
            #print(win32file.ReadFile(hfile,100, None))
            #win32file.SetFilePointer(hfile, 0, win32file.FILE_BEGIN)#FILE_BEGIN,FILE_CURRENT
            #overlapped = pywintypes.OVERLAPPED()
            result, data = win32file.ReadFile(hfile, 512)
            print(result,data)
            #buf = data
            #while len(data) == 512:            
            #    result, data = win32file.ReadFile(hfile, 512, None)
            #    buf += data
            hfile.Close()
    
if __name__ == '__main__':
    #disk_list = get_disk_info()
    #print(disk_list)
    #get_logic_info()
    get_removable_disk()
    
    
#data = os.popen("df -h").read()
#print(data)