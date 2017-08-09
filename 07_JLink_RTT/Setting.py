import os, configparser, winreg

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

def RttSetting():
    settingPath = "../setting.ini"
    if os.path.exists(settingPath):
        conf = configparser.ConfigParser()
        conf.read(settingPath)
        dllPath = conf.get("globals", "Dll_Path")
        mapPath = conf.get("globals", "Map_Path")
        print("dllPath", dllPath)
        print("mapPath", mapPath)
        if False == os.path.exists(dllPath):
            print(dllPath + " is not found.")
            #registrytest(r"Software\SEGGER\J-Link")
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\SEGGER\J-Link")
            InstallPath,d1 = winreg.QueryValueEx(key, u"InstallPath" )
            InstallPath += "JLinkARM.dll"
            print ("InstallPath", InstallPath) 
            conf.set("globals", "Dll_Path", InstallPath)
            conf.write(open(settingPath, 'w'))
            return InstallPath
    else:
        print("Error:setting.ini not found.")
        return 0
        
RttSetting()
