import socket
import config
from ip_header import IPHeader
from ip_packet import IPPacket


bufsize = 1024 * 1024
ip_header_length = 20


def main():

    host = '127.0.1.1'
    
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect((host, config.PROXY_CLIENT_LISTEN_PORT))

    run = True

    while run:
        ip_packet = read_packet(socket)
        #TODO: verify packet
        #TODO: recover from data error




        
def read_packet(socket):
    header_bytes = read_bytes(socket, ip_header_length)
    ip_header = IPHeader(header_bytes)
    payload_bytes = read_bytes(socket, ip_header.raw_length - ip_header_length)
    ip_packet = IPPacket(ip_header, payload_bytes)
    return ip_packet

    

def read_bytes(socket, num_bytes_to_read)
    bytes = ''
    num_bytes_read = 0
    while num_bytes_read < num_bytes_to_read:
         new_bytes =  socket.recv(num_bytes_to_read - num_bytes_read)
         bytes += new_bytes
         num_bytes_read += len(new_bytes)
         
    return bytes
