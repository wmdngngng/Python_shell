import os
import numpy as np
import pylab as plt
#import matplotlib.pyplot as plt

NODE = [46,93,32,57,78,89,44]
COLOR = ['b','g','r','c','m','y','k']
READ_LINE = 10000
RootDir = os.getcwd()



def FilterNode(list_s):
    has_s = []
    for list in list_s:
        for has in has_s:
            if list == has:
                break
        else:
            has_s.append(list)
    return has_s

def Draw_Plot(x_list_s, y_list_s, x_has_list_s, title):
    plt.figure(title[:-4])  #创建图
    for x_has_list in x_has_list_s:  #取出每一个节点
        x_list_value = []  #存放该节点的x轴
        y_list_value = []  #存放该节点的y轴
        i = 0
        for index in range(len(NODE)):
            if x_has_list == NODE[index]:
                color = COLOR[index]
                node = NODE[index]
                break
                
        for x_list in x_list_s:
            if x_list == x_has_list:
                x_list_value.append(i)
                y_list_value.append(y_list_s[i])
            i = i + 1
        plt.plot(x_list_value, y_list_value,'o'+color,label=str(node))
        #print(x_list_value)
        x_list_value = []  #存放该节点的x轴
        y_list_value = []  #存放该节点的y轴
    plt.title(title)  #设置title
    plt.xlabel("Time")
    plt.ylabel("Rssi")
    plt.legend()  #设置图例，与plot里的lable相关
    plt.savefig(title[:-4])
    #plt.show()    
        
        
def ReadFile(dir,name):
    time = 0
    list_rssi = []
    list_node = []
    list_has_node = [] #提取list_node中的节点
    file_dir = os.path.join(dir,name)
    file = open(file_dir)
    lines = file.readlines()  #每个文件读取READ_LINE行
    for line in lines:
        if line[4:8] == "rssi":  #找到每行的rssi
            time = time + 1
            #print(line)
            rssi_value_c = line[9:17]
            node_c = line[32:34]
            rssi_value = int(rssi_value_c,16) #将rssi转16进制
            node = int(node_c,10)  #将node_c转10进制
            list_rssi.append(rssi_value)
            list_node.append(node)
            #print(rssi_value_c,rssi_value,node_c)
    list_has_node = FilterNode(list_node)
    #print(list_node)
    #print(list_rssi)
    print("has node:",list_has_node)  #ok
    Draw_Plot(list_node,list_rssi,list_has_node,name)  
    
            
    #x = range(0,time)
    #plt.plot(x,list_rssi)
    
    
def main():
    for file in os.listdir(RootDir):
        if file.endswith(".log"):  #选取.log文件
            print(file)
            ReadFile(RootDir,file)
        
if __name__ == "__main__":
    main()
