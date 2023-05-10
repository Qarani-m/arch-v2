import socket
import threading
import time


class Client:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = socket.gethostbyname(socket.gethostname())
        self.port = 9090
        self.header_len = 1024
        self.connect = self.client.connect((ip, port))
    def recvMsg(self):
        while True:
            data=self.client.recv(header_len).decode()
            if data.startswith("len"):
                header_len=int(data[3:])
                self.client.send("send".encode())
    def sendData(self):
        self.client.bind((self.ip,self.port))
        self.client.listen(10)
        print("send connection is open")
        while True:
            try:
                conn, addr= self.server.accept()
                print("got a connection from ", addr)
                conn.send(("len"+str(self.getData()[0])).encode())
                conn.close()
            except Exception as e:
                print(e)

client =  Client()
t1 = threading.Thread(target=client.sendData)
t2 = threading.Thread(target=client.recvMsg)

t1.start()
t2.start()