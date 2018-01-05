import subprocess    
import os

Error_Flag = True
Ping_Count = 1

Keyword = ""
IP_s = []
Faild_IP_S = []
INI_Dir = "04_ping_node.ini"

def Format_IP(ip):
    new_ip_s = []
    point = "."
    num_c = 0
    for ip_c in ip.split("."):
        #print(ip_c)
        ip_c = int(ip_c)
        ip_c = str(ip_c)
        new_ip_s.append(ip_c)
    ip = point.join(new_ip_s)
    return ip

def GetConfig_Param():
    ip_s = []
    error_flag = False
    if os.path.exists(INI_Dir):
        f = open(INI_Dir)
        lines = f.readlines()
        f.close()
        for line in lines:
            if -1 != line.find("Ping_Count="):
                ping_count_value = int(line[11:])
                print("Ping_Count=%d"%ping_count_value)
            if -1 != line.find("Keyword="):
                index_start = line.find("\"")
                index_end = line.rfind("\"")
                key_value = line[index_start+1:index_end]
                print("Keyword=\"%s\""%key_value)
            if -1 != line.find("ip="):
                ip_s.append(line[3:])
                print("ip="+line[3:])
        if (ping_count_value > 10) or (ping_count_value <1):
            print("Error:Ping_Count > 10) or (Ping_Count <1")
            error_flag = True
        if len(key_value) == 0:
            print("Error:not find Keyword value.")
            error_flag = True
        if ip_s == []:
            print("Error:not find ip value.")
            error_flag = True
    else:
        print("Error:not find the %s file."%INI_Dir)
        error_flag = True
        ping_count_value = 1
        key_value = "TTL"
        ip_s = ["www.baidu.com","www.baidu.com"]
        
    return error_flag,ping_count_value,key_value,ip_s
        

def GetLinkState(ping_count, keyword, ip_s):
    faild_ip_s = []
    for ip in ip_s:
        #去掉无用的ip地址上为0的字符
        ip = Format_IP(ip)
        #运行ping程序
        arg = "ping.exe %s -n %d"%(ip,ping_count)
        #print(arg)
        p = subprocess.Popen(arg, 
            stdin = subprocess.PIPE, 
            stdout = subprocess.PIPE, 
            stderr = subprocess.PIPE, 
            shell = True)  
        #得到ping的结果
        out = p.stdout.read()  
        out = out.decode('gbk')
        print("---------------------------------------")
        print(out)
        #找出ping成功的关键字TTL
        if out.find(keyword) == -1:  #没有找到关键字TTL
            faild_ip_s.append(ip)
    return faild_ip_s
             
def main():
    sum_ip = 0
    Error_Flag,Ping_Count,Keyword,IP_s = GetConfig_Param()
    if False == Error_Flag:
        Faild_IP_S = GetLinkState(Ping_Count,Keyword,IP_s)
        print("**************************************")
        for faild_ip in Faild_IP_S:
            sum_ip += 1
            print(faild_ip)
        print("sum_ip:%d"%sum_ip)
        
    
if __name__ == '__main__':
    main() 