#pip install pyserial

import serial
from time import sleep
from threading import Thread



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
		data = serial.read_all()
		if data == '':
			continue
		else:
			break
		sleep(0.01)
	return data

def Send_CMD():
	while True:
		tx_header = "A3 3A"
		
		indata = input("input cmd:W [V] [S]\r\n")
		cmd_datas = indata.split(" ")
		cmd_i = 0
		for cmd_data in cmd_datas:
			print(cmd_data)
			if cmd_i == 0:
				if cmd_data == 'w':	#前进
					tx_header.append('A1')
			elif cmd_i == 1:
				tx_header.append(struct.pack('>l',int(cmd_data)))	#大端
			elif cmd_i == 2:
				tx_header.append(struct.pack('>l',int(cmd_data)))
			cmd_i += 1
		serial.write(tx_header)	
	

def UART_Handle():
	Send_CMD()
	data = recv(serial)
	if data != b'':
		print("receive: ",data)
		#serial.write(data)
		
		
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
	t1 = Thread(target=UART_Handle,args=())
	t2 = Thread(target=DRAW_Handle,args=())
	t1.start()
	t2.start()
	
	#while True:
		