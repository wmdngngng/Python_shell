import os

file_path = "uboot_evb.img"
separate1_path = "out1.bin"
separate2_path = "out2.bin"
file_in1_path = "in1.bin"
file_in2_path = "in2.bin"
merge_path  = "merge.bin"


READ_START_SECTOR = 0
READ_END_SECTOR = 1
SECTOR_SIZE = 512

def separate():
    if os.path.exists(file_path):
        file = open(file_path, "rb")
        data = file.read()
        data_out1 = data[(READ_START_SECTOR*SECTOR_SIZE):(READ_END_SECTOR*SECTOR_SIZE)]
        data_out2 = data[(READ_END_SECTOR*SECTOR_SIZE):]
        file_out1 = open(separate1_path, "wb")
        file_out1.write(data_out1)
        file_out1.close()
        file_out2 = open(separate2_path, "wb")
        file_out2.write(data_out2)
        file_out2.close()
        file.close()
    else:
        print(file_path+" is not found.")
    
def merge():
    file_merge = open(merge_path, 'ab')
    file_in1 = open(file_in1_path, 'rb')
    file_in2 = open(file_in2_path, 'rb')
    data_in1 = file_in1.read()
    data_in2 = file_in2.read()
    file_merge.write(data_in1)
    file_merge.write(data_in2)
    file_in1.close()
    file_in2.close()
    file_merge.close()
    
if __name__ == '__main__':
    path_cwd = os.getcwd()
    print(path_cwd)
    os.chdir(path_cwd)
    #separate()
    merge()