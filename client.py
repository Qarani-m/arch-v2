import socket
import threading
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
port = 9090
header_len = 1024            
 
client.connect((ip, port))


data =client.recv(header_len).decode()


print(data)

