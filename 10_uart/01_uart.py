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
global ax5
global ax6
global f

global Name_Str
global finish_data

REPORT_DATA_LEN = 66

DIR_FILE = './'
Right_Data = []
Left_Data = []

R_xs = []
R_v_cur = []
R_err = []
R_err1 = []
R_err2 = []
R_count = []

L_xs = []
L_v_cur = []
L_err = []
L_err1 = []
L_err2 = []
L_count = []

def bcc_off(serial):
	global f
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
	global f
	while True:
		data = serial.readline()
		if data != b'':
			print("rx: ",data,file = f)
		sleep(0.01)
	return data

def Clear_Buf():
	global R_xs
	global R_v_cur
	global L_xs
	global L_v_cur
	
	R_xs = []
	R_v_cur = []
	R_err = []
	R_err1 = []
	R_err2 = []
	R_count = []
	
	L_xs = []
	L_v_cur = []
	L_err = []
	L_err1 = []
	L_err2 = []
	L_count = []
	
def Send_CMD():
	global f
	global Name_Str
	while True:
		tx_header = "A33A"
		tx_buf = tx_header
		indata = input("input cmd:W [V] [S]\r\n")
		cmd_datas = indata.split(" ")
		cmd_i = 0
		flag = 0
		Name_Str = indata
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
			f = open(DIR_FILE+Name_Str+'.txt','w')
			print(tx_buf,file = f)
			tx_buf_b = bytes().fromhex(tx_buf)
			serial.write(tx_buf_b)
			
			Clear_Buf()
		


def UART_Rx_Decode(data):
	global f
	odd_data = ''
	decode_datas = data.split('eeeeeeee')
	for decode_data in decode_datas:
		#print('x:%d ',len(decode_data),decode_data)
		if len(decode_data) == REPORT_DATA_LEN:
			if decode_data[:2] == "01":	#Right_Data
				#print('R:',decode_data)
				Right_Data.append(decode_data)
			elif decode_data[:2] == "02":	#Left_Data
				Left_Data.append(decode_data)
			else:
				print("error:",decode_data,file = f)
		else:
			if decode_data[:2] == "01":
				odd_data = decode_data
			elif decode_data[:2] == "02":
				odd_data = decode_data
			else:
				print("rx: ",decode_data,file = f)
	return odd_data

def UART_Handle():
	global finish_data
	has_data = 0
	count = 0
	last_data = ''
	while True:
		data = serial.readline()
		sleep(0.1)
		
		if data != b'':
			print("...")
			temp = str(binascii.b2a_hex(data))[2:-1]	#str
			last_data = UART_Rx_Decode(last_data+temp)
			has_data = 1
			count = 0
			#finish_data = 0
			#print(temp)
			#print("receive: ",temp)
			#serial.write(data)
		else:
			if 1==has_data:
				count = count+1
				if count > 9:
					finish_data = 1
					has_data = 0
					print("xx")
					
			
def Draw_Init():
	line1.set_data([],[])
	line2.set_data([],[])
	return line1,line2, 

def Draw_Plot():
	global ax1
	global ax2
	global ax3
	global ax4
	global ax5
	global ax6
	global f
	global R_xs
	global R_v_cur
	global finish_data
	
	Err_Count = []
	
	if finish_data == 1:
		r_len = len(Right_Data)
		l_len = len(Left_Data)
		
		if r_len >= l_len:
			min_len = l_len
		else:
			min_len = r_len
		print('len:',r_len,l_len,min_len,file = f)
		for i in range(r_len):
			#print(Right_Data)
			r_y_str = (Right_Data[i])[2:]
			r_y_hex = bytes.fromhex(r_y_str)
			r_num,r_v_dst,r_v_cur,r_err,r_err1,r_err2,r_inc,r_count = struct.unpack('<llllllll',bytes(r_y_hex))
			r_inc = r_inc/30000
			print("r:%5d %8d %8d %8d %8d %8d %8d %8d"%(r_num,r_v_dst,r_v_cur,r_err,r_err1,r_err2,r_inc,r_count),file = f)
			if r_num != 0:
				R_xs.append(r_num)
				R_v_cur.append(r_v_cur)
				R_err.append(r_err)
				R_err1.append(r_err1)
				R_err2.append(r_err2)
				R_count.append(r_count)
		
		for i in range(l_len):
			l_y_str = (Left_Data[i])[2:]
			l_y_hex = bytes.fromhex(l_y_str)
			l_num,l_v_dst,l_v_cur,l_err,l_err1,l_err2,l_inc,l_count = struct.unpack('<llllllll',bytes(l_y_hex))
			l_inc = l_inc/30000
			print('l:%5d %8d %8d %8d %8d %8d %8d %8d'%(l_num,l_v_dst,l_v_cur,l_err,l_err1,l_err2,l_inc,l_count),file = f)
			if l_num != 0:
				L_xs.append(l_num)
				L_v_cur.append(l_v_cur)
				L_err.append(l_err)
				L_err1.append(l_err1)
				L_err2.append(l_err2)
				L_count.append(l_count)
		
		min_len = min_len-5
		for i in range(min_len):
			print(i,R_count[i], L_count[i],file = f)
			Err_Count.append(R_count[i]-L_count[i])
		
		ax1.plot(R_xs,R_v_cur,'b-')
		ax3.plot(R_xs,R_err,'r-',label='err')
		ax3.plot(R_xs,R_err1,'g-',label='err1')		
		ax3.plot(R_xs,R_err2,'b-',label='err2')
		ax5.plot(R_xs,R_count,'r*',label='r_count')
		
		ax2.plot(L_xs,L_v_cur,'b-')
		ax4.plot(L_xs,L_err,'r-',label='err')
		ax4.plot(L_xs,L_err1,'g-',label='err1')
		ax4.plot(L_xs,L_err2,'b-',label='err2')
		ax5.plot(L_xs,L_count,'g*',label='l_count')
		
		ax6.plot(range(min_len),Err_Count,'g.',label='err')
		
		f.close()
		plt.savefig(DIR_FILE+Name_Str+'.png',dpi=100) 
		plt.show()
		finish_data = 0
		print("show")
	
		
def DRAW_Handle():
	global ax1
	global ax2
	global ax3
	global ax4
	global ax5
	global ax6
	fig = plt.figure()
	fig.set_size_inches(18,10,forward=True)
	ax1 = fig.add_subplot(3,2,1)
	ax2 = fig.add_subplot(3,2,2)
	ax3 = fig.add_subplot(3,2,3)
	ax4 = fig.add_subplot(3,2,4)
	ax5 = fig.add_subplot(3,2,5)
	ax6 = fig.add_subplot(3,2,6)
	
	ax1.set_title('Right wheel')
	ax2.set_title('Left wheel')
	ax3.set_title('Right error')
	ax4.set_title('Left error')
	ax4.set_title('Left error')
	ax5.set_title('Count')
	ax6.set_title('Count error')
	
	ax1.grid(True)	#显示网格
	ax2.grid(True)
	ax3.grid(True)
	ax4.grid(True)
	ax5.grid(True)
	ax6.grid(True)
	while True:
		Draw_Plot()
		sleep(0.1)
	
if __name__ == '__main__':
	global finish_data
	global Name_Str
	
	
	serial = serial.Serial('COM5', 115200, timeout=0.5)
	if serial.isOpen():
		print("success")
	else:
		print("failed")
		
	bcc_off(serial)	
	finish_data = 0
	t1 = Thread(target=Send_CMD,args=())
	t2 = Thread(target=UART_Handle,args=())
	t3 = Thread(target=DRAW_Handle,args=())
	t1.start()
	t2.start()
	t3.start()

		