import os
import numpy as np
import pylab as plt
import networkx as nx
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
    
def Rssi2NewworkCost(rssi):
    if rssi >= 1000000:				#less than -80db(zero line), return 1
        return 1
    elif rssi >= 360000 :			#1 ~ 10db(ref -80db as zero, negedge val), return 2  
        return 2			
    elif(rssi >= 114000):			#11~-20db, return 3
        return 3
    elif(rssi >= 35600):			    #21~-30db, return 4
        return 4	
    elif(rssi >= 10300):			    #31~-40db, return 5
        return 5	
    elif(rssi >= 3300):			    #41~-50db,return 5~10
        return 10 - (rssi - 3300)/1400
    elif(rssi >= 800):			    #51~-60db,return 10~20
        return 20 - (rssi - 800)/250
    elif(rssi >= 200):			    #61~-70db,return 20~80
        return 80 - (rssi - 200)/15
    elif(rssi >= 200):			    #71~-80db,return 80~200
        return 200 - (rssi*2 - 400)/3
    else:				                #beyond -80db, treat as unlink,retrun max
        return 0xff

def Draw_NetWork(node,has_nodes):
    G = nx.DiGraph()  #建立一个有向空图
    G.add_node(node)  #加点
    G.add_nodes_from(has_nodes)  #加点的集合
    for has_node in has_nodes:
        G.add_edge(has_node,node,wegiht=4.7,width=6)  #加边
    nx.draw(G,with_labels=True)  #with_labels=True 显示节点名字
        
def Draw_Plot(x_list_s, y_list_s, x_has_list_s, title):
    plt.figure(title[:-4],figsize=(16,8))
    node_base = title[:2]  #本节点
    y_list_value_cal_avg = []  #存放将y轴处理后的值的平均值
    for x_has_list in x_has_list_s:  #取出每一个节点
        x_list_value = []  #存放该节点的x轴
        y_list_value = []  #存放该节点的y轴
        y_list_value_cal = []  #存放将y轴处理后的值
        
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
                temp_cal = Rssi2NewworkCost(y_list_s[i])  #calculation the rssi value
                y_list_value_cal.append(temp_cal)
            i = i + 1
<<<<<<< HEAD
        plt.plot(x_list_value, y_list_value,'.'+color,label=str(node))
        #plt.plot(x_list_value, y_list_value,color,marker = '.',label=str(node))
=======
        plt.subplot(221)  #分成2*2,占第一个图, 第一个参数表示行，第二个参数表示列
        plt.title(title)  #设置title
        plt.ylabel("Rssi")
        plt.plot(x_list_value, y_list_value,'.'+color,label=str(node))
        
        plt.subplot(212)  #分成2*2,占第二个图
        plt.ylabel("Cost")
        plt.xlabel("Time")
        plt.plot(x_list_value, y_list_value_cal,'.'+color,label=str(node))
        temp_avg = np.mean(y_list_value_cal)
        y_list_value_cal_avg.append(temp_avg)  #父节点与子节点的rssi转换后的平均值
        print("Node %d _avg = %d"%(node,temp_avg))
        
        x_list_value = []  #存放该节点的x轴
        y_list_value = []  #存放该节点的y轴
    plt.legend()  #设置图例，与plot里的lable相关
    plt.subplot(222)
    Draw_NetWork(node_base,x_has_list_s)
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
    print("\r")
    Draw_Plot(list_node,list_rssi,list_has_node,name)  
    
    
def main():
    for file in os.listdir(RootDir):
        if file.endswith(".log"):  #选取.log文件
            print(file)
            ReadFile(RootDir,file)
        
if __name__ == "__main__":
    main()
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
    
def Rssi2NewworkCost(rssi):
    if rssi >= 1000000:				#less than -80db(zero line), return 1
        return 1
    elif rssi >= 360000 :			#1 ~ 10db(ref -80db as zero, negedge val), return 2  
        return 2			
    elif(rssi >= 114000):			#11~-20db, return 3
        return 3
    elif(rssi >= 35600):			    #21~-30db, return 4
        return 4	
    elif(rssi >= 10300):			    #31~-40db, return 5
        return 5	
    elif(rssi >= 3300):			    #41~-50db,return 5~10
        return 10 - (rssi - 3300)/1400
    elif(rssi >= 800):			    #51~-60db,return 10~20
        return 20 - (rssi - 800)/250
    elif(rssi >= 200):			    #61~-70db,return 20~80
        return 80 - (rssi - 200)/15
    elif(rssi >= 200):			    #71~-80db,return 80~200
        return 200 - (rssi*2 - 400)/3
    else:				                #beyond -80db, treat as unlink,retrun max
        return 0xff

def Draw_Plot(x_list_s, y_list_s, x_has_list_s, title):
    plt.figure(title[:-4],figsize=(16,8))
    
    for x_has_list in x_has_list_s:  #取出每一个节点
        x_list_value = []  #存放该节点的x轴
        y_list_value = []  #存放该节点的y轴
        y_list_value_cal = []  #存放将y轴处理后的值
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
                temp_cal = Rssi2NewworkCost(y_list_s[i])  #calculation the rssi value
                y_list_value_cal.append(temp_cal)
            i = i + 1
        plt.subplot(211)  #分成2*2,占第一个图, 第一个参数表示行，第二个参数表示列
        plt.title(title)  #设置title
        plt.ylabel("Rssi")
        plt.plot(x_list_value, y_list_value,'.'+color,label=str(node))
        plt.subplot(212)  #分成2*2,占第二个图
        plt.ylabel("Cost")
        plt.xlabel("Time")
        plt.plot(x_list_value, y_list_value_cal,'.'+color,label=str(node))
        
>>>>>>> 02f0f1fd6e6893f0529925ed4aa1172889653aba
        #print(x_list_value)
        x_list_value = []  #存放该节点的x轴
        y_list_value = []  #存放该节点的y轴
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
