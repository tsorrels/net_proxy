import threading
import socket

bufsize = 1024 * 1024

class ServerSocket(object):
    def __init__(self, port):
        self.lock = threading.Lock()
        self.remote_connection = None
        self.remote_addr = None
        
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((socket.gethostname(), port))
        self.socket.listen(1)
                        
    def read(self):
        return self.remote_connection.recv(bufsize)
    
    def write(self, data):
        if self.remote_connection:
            self.remote_connection.sendall(data)

    def fileno(self):
        return self.remote_connection.fileno()

    def accept(self):
        conn, addr = self.socket.accept()
        self.remote_connection = conn
        self.remote_addr = addr
