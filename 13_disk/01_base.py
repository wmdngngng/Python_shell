import os
import wmi
import win32file
import pywintypes
import win32con


def get_disk_info():
    c = wmi.WMI()
    for disk in c.Win32_DiskDrive():
        print("01", disk.Index)     #0,1,2
        print("02", int(disk.Size)/1024/1024/1024)
        print("03", disk.MediaType) #Fixed hard disk media  #Removable Media, usb and sd
        print("04", disk.DeviceID)
        print("05", disk.Name)
        print("06", disk.Caption)
        print("07", disk.Model)
        print("08", disk.InterfaceType)
        print("09", disk.BytesPerSector)
        print("10", disk.TotalSectors)
        print("11", disk.FirmwareRevision)
        print("12", disk.Partitions)
        print("13", disk.TotalTracks)
        print("14", disk.TotalCylinders)
        print("15", disk.SerialNumber)
        print("16", disk.PNPDeviceID)
        
        print("17", disk.Description)
        print("18", disk.Manufacturer)
        print("19", disk.CreationClassName)
        print("20", disk.SystemCreationClassName)
        print("21", disk.SystemName)
        print("22", disk.TotalHeads)
        print("23", disk.SectorsPerTrack)
        print("24", disk.TracksPerCylinder)
        print("25", disk.MediaLoaded)
        print("26", disk.Status)
        print("\n")
        
def get_logic_info():
    c = wmi.WMI()
    for logic in c.Win32_LogicalDisk():
        if logic.Size != None:
            print("01",logic.Caption)    #打印盘符
            print("02",int(logic.Size)/1024/1024/1024)
            print("10",logic.Description)
            print("11",logic.DeviceID)
            print("12",logic.DriveType)
            print("13",logic.FileSystem)
            print("17",logic.MediaType)
            print("18",logic.SerialNumber)
            print("35",logic.VolumeName)
            print("\n")
            
def get_removable_disk():
    index = 0
    disks_list = []
    c = wmi.WMI()
    for disk in c.Win32_DiskDrive():
        if disk.MediaType == "Removable Media":
            tempdisk = {}
            index = index + 1
            print("Index=%d Disk=%d" %(index, disk.Index), disk.InterfaceType,
                "%5.1fG" %(int(disk.Size)/1024/1024/1024))
            tempdisk["index"] = index
            tempdisk["disk"] = disk.Index
            tempdisk["ID"] = disk.DeviceID
            disks_list.append(tempdisk)
    sel_index = input("Please Input Index:")
    for disk_list in disks_list:
        if disk_list["index"] == int(sel_index):
            print("select Disk=%d"%disk_list["disk"])
            disk_name = disk_list["ID"][4:]
            #print(disk_name)
            hfile=win32file.CreateFile("\\\\.\\"+disk_name, win32con.GENERIC_WRITE, 0,None, win32con.OPEN_EXISTING, 0 , None)
            data = "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
            data1 = data + data
            data2 = data1 + data1
            data3 = data2 + data2
            b_hex = data3.encode('ascii')
            print(b_hex)
            win32file.WriteFile(hfile, b_hex)
            hfile.Close()
            hfile=win32file.CreateFile("\\\\.\\"+disk_name, win32con.GENERIC_READ|win32con.GENERIC_WRITE,
                win32con.FILE_SHARE_READ|win32con.FILE_SHARE_WRITE,
                None, win32con.OPEN_EXISTING, 0 , None)
            result, data = win32file.ReadFile(hfile, 512)
            print(result,data)
            hfile.Close()
            
def get_removable_logical():
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
    #get_disk_info()
    get_removable_disk()
    #print(disk_list)
    #get_logic_info()
    #get_removable_disk()
    
    
#data = os.popen("df -h").read()
#print(data)