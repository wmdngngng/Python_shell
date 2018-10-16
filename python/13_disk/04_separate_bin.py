import os

file_path = "uboot_evb.img"
file_out_path = "out.bin"

READ_START_SECTOR = 0
READ_END_SECTOR = 1
SECTOR_SIZE = 512

def separate():
    if os.path.exists(file_path):
        file = open(file_path, "rb")
        data = file.read()
        data_out = data[(READ_START_SECTOR*SECTOR_SIZE):(READ_END_SECTOR*SECTOR_SIZE)]
        file_out = open(file_out_path, "wb")
        file_out.write(data_out)
        file_out.close()
        file.close()
    else:
        print(file_path+" is not found.")
    

if __name__ == '__main__':
    path_cwd = os.getcwd()
    print(path_cwd)
    os.chdir(path_cwd)
    separate()