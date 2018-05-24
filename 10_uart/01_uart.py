#pip install pyserial

import serial
import struct
import binascii
import numpy as np
from time import sleep
from threading import Thread
from matplotlib import pyplot as plt
from matplotlib import animation




def bcc_off(serial):
	serial.write(bytes.fromhex('A3 3A 00 01 01 00'))
	while True:
		flag = 0
		while serial.inWaiting()>0:
			data = serial.readline()
			print(data,len(data))
			if data[:6] == b'\xA3\x3A\x00\x01\x00\x01':
				print("bcc off")
				flag = 1
				break
		if flag == 1:
			break
	

def recv(serial):
	while True:
		data = serial.readline()
		#data = serial.read_all()
		#if data == '':
		#	continue
		#else:
		#	break
		if data != b'':
			print("rx: ",data)
		sleep(0.01)
	return data

def Send_CMD():
	while True:
		tx_header = "A33A"
		tx_buf = tx_header
		indata = input("input cmd:W [V] [S]\r\n")
		cmd_datas = indata.split(" ")
		cmd_i = 0
		for cmd_data in cmd_datas:
			print(cmd_data)
			if cmd_i == 0:
				if cmd_data == 'w':	#前进
					tx_buf += "A1"
			elif cmd_i == 1:
				bytes_hex1 = struct.pack('>l',int(cmd_data))#大端
				str_data1 = str(binascii.b2a_hex(bytes_hex1))[2:-1]
				tx_buf += str_data1
			elif cmd_i == 2:
				bytes_hex2 = struct.pack('>l',int(cmd_data))
				str_data2 = str(binascii.b2a_hex(bytes_hex2))[2:-1]
				tx_buf += str_data2
			cmd_i += 1
		print(tx_buf)
		tx_buf_b = bytes().fromhex(tx_buf)
		serial.write(tx_buf_b)
		sleep(1)
	

def UART_Handle():
	while True:
		data = serial.readline()
		if data != b'':
			print("receive: ",data)
			serial.write(data)
		
		
def DRAW_Handle():
	while True:
		sleep(10)
		#print("hello")
	
if __name__ == '__main__':
	serial = serial.Serial('COM1', 115200, timeout=0.5)
	if serial.isOpen():
		print("success")
	else:
		print("failed")
		
	bcc_off(serial)	
	t1 = Thread(target=Send_CMD,args=())
	t2 = Thread(target=UART_Handle,args=())
	t3 = Thread(target=DRAW_Handle,args=())
	t1.start()
	t2.start()
	t3.start()
	
	#while True:
		