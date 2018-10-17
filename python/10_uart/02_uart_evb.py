import serial
import binascii
import time

com_port = 'COM3'

serial_com = serial.Serial(com_port, 115200, timeout=0.5)
if serial_com.isOpen():
    print(com_port+" is open success.")
else:
    exit(com_port+"is open faild!")
#serial_com.write("root\n".encode("gbk"))
#time.sleep(2)
count_rst = 0
while True:
    data = serial_com.readline()
    if data != b'':
        data_str = bytes(data).decode('ascii')
        print('*', end="")
        #print(data_str)
        if data_str[:16] == "localhost login:":
            count_rst = count_rst + 1
            print("\r\nreset count : %d"%(count_rst))
            time.sleep(1)
            serial_com.write("root\n".encode("gbk"))
        if data_str[:17] == "root@localhost:/#":
            time.sleep(120)
            serial_com.write("reboot\n".encode("gbk"))