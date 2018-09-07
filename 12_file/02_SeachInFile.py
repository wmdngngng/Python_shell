import os
import sys

LOG_FILE = "02_D.log"
STR_FILE = "02_train.strings"
OUT_FILE = "02_out.log"

Out_Buf = []

if __name__ == '__main__':
	print("\r\nInput file: "+LOG_FILE+"  "+STR_FILE+"\r\n")
	f_log = open(LOG_FILE)
	f_str = open(STR_FILE)
	f_out = open(OUT_FILE,"w+")
	lines_log = f_log.readlines()
	lines_str = f_str.readlines()
	f_log.close()
	f_str.close()
	log_i=0
	for logs in lines_log:
		log_i = log_i+1
		log_index = logs[19:24]
		log_num = logs[27:37]
		#print(log_index,log_num,log_i)
		if log_index == "index":
			print("log num:",log_i)
			str_i=0
			for str in lines_str:
				str_i = str_i + 1
				if log_num == str[0:10]:
					str_next = str[11:]
					print(str[0:10],str_next)
					Out_Buf.append(logs[:-1]+"  //"+str_next)
		else:
			Out_Buf.append(logs)
	for out in Out_Buf:
		f_out.write(out)
	f_out.close()
		