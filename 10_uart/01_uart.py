#pip install pyserial

import serial
import struct
import binascii
import numpy as np
from time import sleep
from threading import Thread
from matplotlib import pyplot as plt
from matplotlib import animation

REPORT_DATA_LEN = 50
Right_Data = []
Left_Data = []


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
		flag = 0
		for cmd_data in cmd_datas:
			print(cmd_data)
			if cmd_i == 0:
				if cmd_data == 'w':	#前进
					tx_buf += "A1"
					tx_buf += "08"
			elif cmd_i == 1:
				bytes_hex1 = struct.pack('>l',int(cmd_data))#大端
				str_data1 = str(binascii.b2a_hex(bytes_hex1))[2:-1]
				tx_buf += str_data1
			elif cmd_i == 2:
				bytes_hex2 = struct.pack('>l',int(cmd_data))
				str_data2 = str(binascii.b2a_hex(bytes_hex2))[2:-1]
				tx_buf += str_data2
				flag = 1
			cmd_i += 1
		if flag == 1:
			print(tx_buf)
			tx_buf_b = bytes().fromhex(tx_buf)
			serial.write(tx_buf_b)
		sleep(1)
		


def UART_Rx_Decode(data):
	odd_data = ''
	decode_datas = data.split('eeeeeeee')
	for decode_data in decode_datas:
		if len(decode_data) == REPORT_DATA_LEN:
			if decode_data[:2] == "01":	#Right_Data
				Right_Data.append(decode_data)
			elif decode_data[:2] == "02":	#Left_Data
				Left_Data.append(decode_data)
			else:
				print("error:",decode_data)
		else:
			if decode_data[:2] == "01":
				odd_data = decode_data
			elif decode_data[:2] == "02":
				odd_data = decode_data
			else:
				print("rx: ",decode_data)
	return odd_data

def UART_Handle():
	last_data = ''
	while True:
		data = serial.readline()
		sleep(0.01)
		
		if data != b'':
			temp = str(binascii.b2a_hex(data))[2:-1]	#str
			last_data = UART_Rx_Decode(last_data+temp)
			#print(temp)
			#print("receive: ",temp)
			#serial.write(data)

def Draw_Init():
	line1.set_data([],[])
	line2.set_data([],[])
	return line1,line2, 
	
def Draw_Animate(i):
	x1 = np.linspace(0,1,2000)
	x2 = np.linspace(0,1,2000)
	y1 = 
	y2 = 
	line1.set_data(x1,y1)
	line2.set_data(x2,y2)
	return line1,line2,
			
def Draw_Plot():
	fig = plt.figure()
	ax1 = fig.add_subplot(2,1,1, xlim=(0,2000), ylim=(0,500000))
	ax2 = fig.add_subplot(2,1,1, xlim=(0,2000), ylim=(0,500000))
	line1, = ax1.plot([],[],lw=2)
	line2, = ax2.plot([],[],lw=2)
	
	animate = animation.FuncAnimation(fig, Draw_Animate, init_func=Draw_Init, frames=50, interval=10)
	plt.show

		
def DRAW_Handle():
	while True:
		sleep(0.01)
		if Right_Data != []:
			if Right_Data[0] != '':
				print('R:',Right_Data[0])
				del Right_Data[0]
		if Left_Data != []:
			if Left_Data[0] != '':
				print('L:',Left_Data[0])
				del Left_Data[0]
		#print("hello")
	
if __name__ == '__main__':
	serial = serial.Serial('COM5', 115200, timeout=0.5)
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
		