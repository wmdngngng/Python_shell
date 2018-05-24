import os

HasNode_Dir = "02has_node.log"

BaseNodes = [75, 88, 65, 90, 96, 66, 85,
            43, 31,  9, 93, 84, 44, 56, 17,
             3, 70, 73, 27, 64, 39, 18, 59,
            69, 19, 16, 80, 14, 29,
            92, 62, 63, 86, 42,  8,
            97, 41, 82, 11, 51, 99, 55,
            79, 94, 15, 45, 57, 60, 20, 35,
            48, 83,  4, 81] 

HasNodes = []
AddNodes = []
LossNodes = []


def GetBaseNode():
    sum = 0
            
def GetHasNode():
    has_nodes = []
    temp_has_nodes = []
    if os.path.exists(HasNode_Dir):
        f = open(HasNode_Dir)
        lines = f.readlines()
        for line in lines:
            index = line.find("Destination")
            #print(index)
            if 21 == index:
                node = line[15:17]
                #print(node)
                temp_has_nodes.append(node)
        f.close()
        for temp_has_node in temp_has_nodes:
            if 0 == len(has_nodes):
                has_nodes.append(temp_has_node)
            else:
                for has_node in has_nodes:
                    if temp_has_node == has_node:
                        break
                else:
                    has_nodes.append(temp_has_node)
        return has_nodes
    else:
        print("Error: not find the has_node.log file.")

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
    print("sum BaseNode = ",base_num)
    print("sum HasNode  = ",has_num)
    print("sum LostNode = ",loss_sum)
    print("sum AddNode  = ",add_num)
    print("Lost Node as follow:")
    for loss_node in loss_nodes:
        print(loss_node)
    if (has_num + loss_sum) > base_num:
        print("Add Node as follow:")
        for add_node in add_nodes:
            print(add_node)
                
def main():
    GetBaseNode()
    HasNodes = GetHasNode()
    CompareNode(BaseNodes, HasNodes)
    
    
if __name__ == '__main__':
    main()