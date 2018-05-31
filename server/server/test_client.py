
import socket
import config

HOST = socket.gethostname()
PORT = config.HOST_CLIENT_LISTEN_PORT
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall('Hello, world')
data = s.recv(1024)
s.close()
print 'Received', repr(data)
