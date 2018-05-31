import socket
import config


bufsize = 1024 * 1024

def main():

    host = '127.0.1.1'
    
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect((host, config.PROXY_CLIENT_LISTEN_PORT))

    run = True

    while run:
        data = socket.recv(bufsize)
        




        
