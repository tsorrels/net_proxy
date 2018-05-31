import socket
import config
import threading
import server_socket
import time
import select


def main():
    print "server running"
    
    host_socket = server_socket.ServerSocket(config.HOST_CLIENT_LISTEN_PORT)

    proxy_socket = server_socket.ServerSocket(config.PROXY_CLIENT_LISTEN_PORT)

    proxy_args = (proxy_socket, host_socket)
    proxy_client_thread = threading.Thread(target = run, args = proxy_args)

    host_args = (host_socket, proxy_socket)
    host_client_thread = threading.Thread(target = run, args = host_args)

    addr = socket.gethostname()
    print "Listening to ", addr, ":", config.HOST_CLIENT_LISTEN_PORT
    print "Listening to ", addr, ":", config.PROXY_CLIENT_LISTEN_PORT
    
    proxy_client_thread.daemon = True
    host_client_thread.daemon = True
    
    proxy_client_thread.start()
    host_client_thread.start()
    
    while (True):
        print '.',
        time.sleep(10)
        
    
def run(read_socket, write_socket):
    listen = True
    while (listen):
        read_socket.accept()
        print "accepted connection"
        execute(read_socket, write_socket)
        

def execute(read_socket, write_socket):
    run = True
    while (run):
        print "running in main loop"
        ready = select.select([read_socket], [], [], None)
        read_sockets = ready[0]
        if read_sockets:
            socket = read_sockets[0]
            data = socket.read()
            if not data:
                break
            print data
            write_socket.write(data)
