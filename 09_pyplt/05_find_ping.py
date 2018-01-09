import subprocess    
import os

Key_names = ["Ping_Count","Keyword","Ping_IP","Log_Dir","Master_IP"]
MAC_name = "mac"
Config_Name = "05_config.ini"

def Find_Word(str,word):
    if -1 != str.find(word):
        index_start = str.find("\"")
        index_end = str.rfind("\"")
        key_value = str[index_start+1:index_end]
        print(key_value)
    else:
        key_value = "False"
    return key_value

def Get_Config():
    error_flag = False
    curr_dir = os.getcwd()
    cfg_dir = os.path.join(curr_dir,Config_Name)
    
    key_sum = 0
    for key_name in Key_names:
        key_sum += 1
    
    if os.path.exists(cfg_dir):
        mac_s = []
        f = open(cfg_dir)
        lines = f.readlines()
        f.close()
        error_flag = False
        for line in lines:
            for key_name in Key_names:
                value = Find_Word(line, key_name)
                if "False" != value:
                    if key_name == "Ping_Count":
                        ping_count_v = int(value)
                        if (ping_count_v > 100) or (ping_count_v < 1):
                            print("Error:Ping_Count > 10) or (Ping_Count <1")
                            error_flag = True
                    if key_name == "Keyword":
                        keyword_v = value
                    if key_name == "Ping_IP":
                        ping_ip_v = value
                        if (ping_ip_v != "True") and (ping_ip_v != "False"):
                            print("Ping_IP shuld be True or False.")
                            error_flag = True
                    if key_name == "Log_Dir":
                        log_dir_v = value
                    if key_name == "Master_IP":
                        master_ip_v = value
                    key_sum -= 1
            if 0 == key_sum:
                break
                
        for line in lines:
            mac_v = Find_Word(line, MAC_name)
            if mac_v != "False":
                mac_s.append(mac_v)
    else:
        print("Error:not find the %s file."%cfg_name)
        error_flag = True
        ping_count_v = 4
        keyword_v = ""
        ping_ip_v = ""
        log_dir_v = ""
        master_ip_v = ""
        mac_s = []
    return error_flag, ping_count_v, keyword_v, ping_ip_v,log_dir_v,master_ip_v,mac_s

def Get_Short_MAC(mac_s):
    short_mac_s = []
    for mac in mac_s:
        index = mac.rfind("-")
        value = mac[index+1:]
        short_mac_s.append(int(value))
    return short_mac_s
    
def Get_Log_MAC(log_dir):
    error_flag = False
    short_mac_logs = []
    if os.path.exists(log_dir):
        f = open(log_dir)
        lines = f.readlines()
        f.close()
        for line in lines:
            index = line.find("Destination")
            if 21 == index:
                value = line[15:17]
                short_mac_logs.append(int(value))
    else:
        print("Error:not find %s."%log_dir)
        error_flag = True
    if short_mac_logs == []:
        print("Error:there have no Destination addr in %s"%log_dir)
    return error_flag, short_mac_logs

def CompareNode(base_nodes, has_nodes):
    add_nodes = []
    loss_nodes = []
    add_num = 0
    loss_sum = 0
    base_num = 0
    has_num = 0
    for base_node in base_nodes:
        for has_node in has_nodes:
            if base_node == int(has_node):
                break
        else:
            loss_nodes.append(base_node)
            
    for base_node in base_nodes:
        base_num += 1
    for has_node in has_nodes:
        has_num += 1
    for loss_node in loss_nodes:
        loss_sum += 1
    
    if (has_num + loss_sum) > base_num:
        for has_node in has_nodes:
            for base_node in base_nodes:
                if int(has_node) == base_node:
                    break
            else:
                add_nodes.append(has_node)
                add_num += 1
    #print("sum BaseNode = ",base_num)
    #print("sum HasNode  = ",has_num)
    #print("sum LostNode = ",loss_sum)
    #print("sum AddNode  = ",add_num)
    #print("Lost Node as follow:")
    #for loss_node in loss_nodes:
    #    print(loss_node)
    #if (has_num + loss_sum) > base_num:
    #    print("Add Node as follow:")
    #    for add_node in add_nodes:
    #        print(add_node)
    return loss_nodes,add_nodes

            
def Get_IP(ip,short_mac_s):
    ip_s = []
    index = ip.rfind(".")
    ip_net = ip[:index+1]
    for short_mac in short_mac_s:
        short_mac = int(short_mac)
        short_mac = str(short_mac)
        ip_s.append(ip_net+short_mac)
    return ip_s

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
    
def GetLinkState(ping_count, keyword, ip_s):
    faild_ip_s = []
    sum_ip = 0
    faild_num = 0
    for ip in ip_s:
        sum_ip += 1
        #去掉无用的ip地址上为0的字符
        ip = Format_IP(ip)
        #运行ping程序
        arg = "ping.exe %s -n %d"%(ip,ping_count)
        print(arg)
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
            faild_num += 1
    return sum_ip,faild_num, faild_ip_s

def Get_Print(ping,base_s,mac_s,loss_s,add_s,faild_s):
    base_num = mac_num = loss_num = add_num = 0
        
    for base in base_s:
        base_num += 1
    for mac in mac_s:
        mac_num += 1
    for loss in loss_s:
        loss_num += 1
    for add in add_s:
        add_num += 1

    print("**************************************")
    print("BaseNode  = %d"%base_num)
    print("HasNode   = %d"%mac_num)
    print("LossNode  = %d"%loss_num)
    print("AddNode   = %d"%add_num)
    if ping == "True":
        faild_num = 0
        for faild in faild_s:
            faild_num += 1
        print("FaildNode = %d"%faild_num)
        
    if loss_num > 0:
        print("Loss Node as follow:")
        for loss in loss_s:
            print(loss)
    if add_num > 0:
        print("Add Node as follow:")
        for add in  add_s:
            print(add)
    if ping == "True":
        if faild_num > 0:
            print("Ping faild ip as follow:")
            for faild in faild_s:
                print(faild)
    print("**************************************")
    
    
def main():
    error_flag, ping_count_v, Keyword_V, ping_ip_v,log_dir_v,master_ip_v,mac_s = Get_Config()
    if False == error_flag:
        short_mac_base_s = Get_Short_MAC(mac_s)
        error_flag, short_mac_have_s = Get_Log_MAC(log_dir_v)
        if False == error_flag:
            loss_nodes,add_nodes = CompareNode(short_mac_base_s, short_mac_have_s)
            if ping_ip_v == "True":
                ip_s = Get_IP(master_ip_v,short_mac_have_s)
                sum_ip,sum_faild, faild_ip_s = GetLinkState(ping_count_v, Keyword_V, ip_s)
            Get_Print(ping_ip_v,short_mac_base_s,short_mac_have_s,loss_nodes,add_nodes,faild_ip_s)
        
    
if __name__ == '__main__':
    main() 