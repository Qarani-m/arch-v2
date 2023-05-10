import socket
import pyautogui as pag
import time
import threading


class Server:
    def __init__(self):
        self.byteSize = 64
        self.port = 9090
        self.ip = socket.gethostbyname(socket.gethostname())
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def getData(self):
        time.sleep(10)
        pag.screenshot("file.png")
        with open("file.png", "rb") as file:
            data = file.read()
        pic_length =len(data)
        return [pic_length]
    def recvMsg(self):
        self.server.connect((self.ip,self.port))
        header_len= 2048
        data = self.server.recv(header_len).decode
        if data:
            self.sendData
    def sendData(self):
        self.server.bind((self.ip,self.port))
        self.server.listen(10)
        print("seeking connection")
        while True:
            try:
                conn, addr= self.server.accept()
                print("got a connection from ", addr)
                conn.send(("len"+str(self.getData()[0])).encode())
                conn.close()
            except Exception as e:
                print(e)
sender = Server()
t1 = threading.Thread(target=sender.sendData)

t2 = threading.Thread(target=sender.recvMsg)

t1.start()
time.sleep(10)
t2.start()