# 说明：python pyserial study
# 1. 
# 2. 
# 3. 
# 4. 
# 5. 
# 6. 
#
# @Author: labc
# Created on June 30 2017
#
#
import serial
import serial.tools.list_ports

PortLists = list(serial.tools.list_ports.comports())

if len(PortLists) <= 0:
    print ("the serial port can not find!")
else:
    for portlist in PortLists:
        print ("port:",portlist)
    '''print ("serial port num:", len(PortList))
    portlist0 = list(PortList[0])
    portserial = portlist0[0]
    print (portserial)
    ser = serial.Serial(portserial,9600,timeout = 60)
    print ("The port is really use>",ser.name)
    ser.write(b"Hello World!\r\n")'''