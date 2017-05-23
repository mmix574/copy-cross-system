# CLIENT
import socket 
import pyperclip
import time
import multiprocessing

connect_address = ('192.168.1.66',1111)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

memory_clipboard = ""
def update():
	global memory_clipboard
	if memory_clipboard == pyperclip.paste():
		return False,""
	else:
		memory_clipboard = pyperclip.paste()
		return True,memory_clipboard
i = 0
while True:
	u,content = update()
	# u,content = True,input('input:')
	if u:
		s.sendto(content.encode('utf-8'),connect_address)
		data,addr = s.recvfrom(2048)
	else:
		s.sendto(b'',connect_address)
		data,addr = s.recvfrom(2048)
		content = data.decode('utf-8')
		memory_clipboard = content
		while pyperclip.paste()!=content:
			pyperclip.copy(content)
	print(i,data,addr)
	i = i+1
	time.sleep(0.9)
s.close()
