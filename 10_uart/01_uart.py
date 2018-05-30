#pip install pyserial

import serial
import struct
import binascii
import numpy as np
from time import sleep
from threading import Thread
from matplotlib import pyplot as plt
from matplotlib import animation

global ax1
global ax2
global ax3
global ax4

REPORT_DATA_LEN = 58
Right_Data = []
Left_Data = []

R_xs = []
R_v_cur = []
R_err = []
R_err1 = []
R_err2 = []

L_xs = []
L_v_cur = []
L_err = []
L_err1 = []
L_err2 = []

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

def Clear_Buf():
	global R_xs
	global R_v_cur
	global L_xs
	global L_v_cur
	
	R_xs = []
	R_v_cur = []
	L_xs = []
	L_v_cur = []
	
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
			
			Clear_Buf()
			
			
		#sleep(1)
		


def UART_Rx_Decode(data):
	odd_data = ''
	decode_datas = data.split('eeeeeeee')
	for decode_data in decode_datas:
		if len(decode_data) == REPORT_DATA_LEN:
			if decode_data[:2] == "01":	#Right_Data
				#print('R:',decode_data)
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
		#sleep(0.01)
		
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
	global ax1
	global ax2
	global ax3
	global ax4
	global R_xs
	global R_v_cur
	
	if Right_Data != []:
		if Right_Data[0] != '':
			r_y_str = (Right_Data[0])[2:]
			r_y_hex = bytes.fromhex(r_y_str)
			#print(Right_Data[0])
			r_num,r_v_dst,r_v_cur,r_err,r_err1,r_err2,r_inc = struct.unpack('<lllllll',bytes(r_y_hex))
			r_inc = r_inc/30000
			print("r:%5d %8d %8d %8d %8d %8d %10d"%(r_num,r_v_dst,r_v_cur,r_err,r_err1,r_err2,r_inc))
			del Right_Data[0]
			if r_num != 0:
				R_xs.append(r_num)
				R_v_cur.append(r_v_cur)
				R_err.append(r_err)
				R_err1.append(r_err1)
				R_err2.append(r_err2)
	
	if Left_Data != []:
		if Left_Data[0] != '':
			l_y_str = (Left_Data[0])[2:]
			l_y_hex = bytes.fromhex(l_y_str)
			l_num,l_v_dst,l_v_cur,l_err,l_err1,l_err2,l_inc = struct.unpack('<lllllll',bytes(l_y_hex))
			l_inc = l_inc/30000
			print('l:%5d %8d %8d %8d %8d %8d %10d'%(l_num,l_v_dst,l_v_cur,l_err,l_err1,l_err2,l_inc))
			del Left_Data[0]
			if l_num != 0:
				L_xs.append(l_num)
				L_v_cur.append(l_v_cur)
				L_err.append(l_err)
				L_err1.append(l_err1)
				L_err2.append(l_err2)
			
	#ax1.clear()
	ax1.plot(R_xs,R_v_cur,'b-')
	ax3.plot(R_xs,R_err,'r-',label='err')
	ax3.plot(R_xs,R_err1,'g-',label='err1')		
	ax3.plot(R_xs,R_err2,'b-',label='err2')
	
	ax2.plot(L_xs,L_v_cur,'b-')
	ax4.plot(L_xs,L_err,'r-',label='err')
	ax4.plot(L_xs,L_err1,'g-',label='err1')
	ax4.plot(L_xs,L_err2,'b-',label='err2')

		
def DRAW_Handle():
	global ax1
	global ax2
	global ax3
	global ax4
	fig = plt.figure()
	ax1 = fig.add_subplot(2,2,1)
	ax2 = fig.add_subplot(2,2,2)
	ax3 = fig.add_subplot(2,2,3)
	ax4 = fig.add_subplot(2,2,4)
	ax1.set_title('Right wheel')
	ax2.set_title('Left wheel')
	ax3.set_title('Right error')
	ax4.set_title('Left error')
	ax1.grid(True,color='k')	#显示网格
	ax2.grid(True,color='k')
	ax3.grid(True,color='k')
	ax4.grid(True,color='k')
	#animate = animation.FuncAnimation(fig, Draw_Animate, init_func=Draw_Init, frames=50, interval=10)
	animate = animation.FuncAnimation(fig, Draw_Animate, interval=100)
	plt.show()
	
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
		