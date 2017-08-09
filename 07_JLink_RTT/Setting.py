import os, configparser, winreg

def registrytest(keypath):
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
        if False == os.path.exists(dllPath):
            print(dllPath + " is not found.")
            print(registrytest(r"Software\SEGGER\J-Link"))
            #key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\SEGGER\J-Link")
            #print(key)
        print(dllPath)
        print(mapPath)
            
    else:
        print("Error:setting.ini not found.")
        
RttSetting()
