import socket
import pyautogui as pag
import time
import threading
port = 9090
ip = socket.gethostbyname(socket.gethostname())
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class Server:
    def __init__(self):
        self.byteSize = 64
    def getData(self):
        time.sleep(10)
        pag.screenshot("file.png")
        with open("file.png", "rb") as file:
            data = file.read()
        pic_length =len(data)
        return [pic_length]
    def sendData(self):
        server.bind((ip,port))
        server.listen(10)
        print("seeking connection")
        while True:
            try:
                conn, addr= server.accept()
                print("got a connection from ", addr)
                conn.send(str(self.getData()[0]).encode())
                conn.close()
            except Exception as e:
                print(e)
sender = Server()
sender.sendData()