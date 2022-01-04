import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80)) # this is not like sending the data, just like dialing the phone.
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode() # encode converts 'unicode' to 'utf-8'
mysock.send(cmd)

while True:
	data = mysock.recv(512) # receive upto 512 characters
	if (len(data) < 1): # if there is no data, which means the end of the file.
		break
	print(data.decode())
mysock.close()