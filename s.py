# SERVER
import socket
import pyperclip
import time

local_address = ("0.0.0.0",1111)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(local_address)


memory_clipboard = ""
def update():
	global memory_clipboard
	past = pyperclip.paste()

	if not len(past):
		while pyperclip.paste()!=memory_clipboard:
			pyperclip.copy(memory_clipboard)
		return False,memory_clipboard

	if memory_clipboard == past:
		return False,memory_clipboard
	else:
		memory_clipboard = past
		return True,memory_clipboard

i = 1
while True:
	data,addr = s.recvfrom(2048)
	c,clip = update()
	print(i,c,clip)
	if not data:
		s.sendto(memory_clipboard.encode('utf-8'),addr)
	else:
		content = data.decode('utf-8')
		memory_clipboard = content
		while pyperclip.paste()!=content:
			pyperclip.copy(content)
		s.sendto(content.encode('utf-8'),addr)
	print(i,data,addr)
	i = i+1