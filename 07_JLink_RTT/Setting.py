import os, configparser, winreg

DllPath = "Dll_Path"
MapPath = "Map_Path"

def RegSeach(keypath):
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, keypath, 0, winreg.KEY_ALL_ACCESS)
    try:
        i = winreg.QueryInfoKey(key)[0]  #sub keys 
        for j in range( 0, i):
            subkey_name = winreg.EnumKey(key, j)
            print ("1:", subkey_name)
            subkey = winreg.OpenKey(key, subkey_name)
            try:
                m = winreg.QueryInfoKey(subkey)[1]  #values 
                print ("2:", m)
                for n in range( 0, m):
                    print ("3:", winreg.EnumValue(subkey, n))
                InstallPath,d1 = winreg.QueryValueEx(subkey, u"InstallPath" )
                print ("4:", InstallPath,d1)
            except Exception:
                print ("exception")
            winreg.CloseKey(subkey)
    except WindowsError:
        print ("exception")
    finally:
        winreg.CloseKey(key)


def getSetting(key):
    settingPath = "../setting.ini"
    if os.path.exists(settingPath):
        conf = configparser.ConfigParser()
        conf.read(settingPath)
        if key == MapPath:
            mappath_value = conf.get("globals", MapPath)
            if ".map" == mappath_value[-4:]:
                if os.path.exists(mappath_value):
                    return mappath_value
                else:
                    print(mappath_value + " is not found.")
                    return 0
            else:
                print(mappath_value + " have no map")
                return 0
                
        elif key == DllPath:
            dllpath_value = conf.get("globals", DllPath)
            if False == os.path.exists(dllpath_value):
                print(dllpath_value + " is not found.")
                #registrytest(r"Software\SEGGER\J-Link")
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\SEGGER\J-Link")
                InstallPath,d1 = winreg.QueryValueEx(key, u"InstallPath" )
                InstallPath += "JLinkARM.dll"
                if os.path.exists(InstallPath):   
                    print ("InstallPath", InstallPath) 
                    conf.set("globals", "Dll_Path", InstallPath)
                    conf.write(open(settingPath, 'w'))
                    return InstallPath
                else:
                    print("JLinkARM.dll not found in regedit")
                    return 0
            else:
                return dllpath_value
        else:
            print(key+" is not found in "+settingPath)
            return 0
       
    else:
        print("Error:setting.ini not found.")
        return 0
        
print("DllPath", getSetting(DllPath))
print("MapPath", getSetting(MapPath))
