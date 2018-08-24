import os
import binascii

FILE_PATH = "./00.bin"	#目标文件路径
UNIT_BYTE = 2	#头文件 UNIT_BYTE 字节为一组

if __name__ == '__main__':
	print("\r\nThe function is bin to .h file.\r\n")
	if os.path.exists(FILE_PATH):
		f_i = open(FILE_PATH,"rb")
		f_o = open("00.h", "r+")	#可读；可写；可追加
		
		if UNIT_BYTE == 2:
			f_o.write("unsigned short const array[] = {\n")
		lines = f_i.readlines()
		print(lines)
		for line in lines:
			#print("line:",line)
			line_str = str(binascii.b2a_hex(line))[2:-1]
			print(line_str)
			lens = len(line_str)
			unit_count = UNIT_BYTE*2
			lens_for = int(lens/unit_count)
			print("len:",lens,unit_count,lens_for)
			for i in range(0,lens_for):
				unit_byte = line_str[:4]
				line_str = line_str[4:]
				print(unit_byte)
				f_o.write(unit_byte+",\n")
		
		f_o.write("};\n")
	else:
		print("please edit the input file name as 00.bin.")