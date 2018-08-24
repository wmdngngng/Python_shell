import os
import binascii

UNIT_BYTE = 2	#头文件 UNIT_BYTE 字节为一组

def Find_Bin_File():
	filenames = []
	cur_dir = os.getcwd()
	for file in os.listdir(cur_dir):
		if file[-4:] == ".bin":
			filename = file[:-4]
			#print(filename)
			filenames.append(filename)
	return filenames

if __name__ == '__main__':
	print("\r\nThe function is bin to .h file.\r\n")
	filenames = Find_Bin_File()
	if filenames == []:
		print("ERROR: not find the file in courrent list.")
	else:	
		for filename in filenames:
			print("file name:",filename)
			f_i = open(filename+".bin","rb")
			f_o = open(filename+".h", "w+")
		
			if UNIT_BYTE == 2:
				f_o.write("unsigned short const array[] = {\n")
			lines = f_i.read()
			print(lines)
			#for line in lines:
			#print("line:",line)
			line_str = str(binascii.b2a_hex(lines))[2:-1]
			print(line_str)
			lens = len(line_str)
			unit_count = UNIT_BYTE*2
			lens_for = int(lens/unit_count)
			for i in range(0,lens_for):
				unit_byte = line_str[:4]
				line_str = line_str[4:]
				print(unit_byte)
				f_o.write("0x"+unit_byte+",\n")
			
			f_o.write("};\n")
			print("len:",lens,unit_count,lens_for)