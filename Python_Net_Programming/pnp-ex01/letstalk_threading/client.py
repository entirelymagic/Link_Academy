import socket
import threading
import sys
import os

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
rooms = {}


class ChatListener(threading.Thread):
    username = ""

    def __init__(self, username, ip):
        super().__init__()
        self.username = username
        self.ip = self.ip

    def run(self):
        client.connect(("127.0.0.1", 8005))
        client.send(self.username.encode("utf-8"))
        while True:
            res = client.recv(1024).decode("utf-8")
            if res != "":
                print(f"\r\n{res}")
                print("Enter message: ", end="", flush=True)


username = input("Enter username: ")


class AdvertisorClient(threading.Thread):
    def __init__(self):
        super().__init__()
        self.udpAdv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udpAdv.bind(("0.0.0.0", 8005))

    def run(self):

        while True:
            msg = self.udpAdv.recvfrom(16)
            chatPort = msg[0].decode("utf-8")
            chatIP = msg[1][0]
            rooms[chatIP] = chatPort


adv = AdvertisorClient()
adv.daemon = True
adv.start()


while True:
    os.system("cls")
    print("Available chat rooms: \n")
    for k, v in rooms.items():
        print(f"Chat server {k} available on port {v}")
        chatserverRoom = input("Which room you would like to join ?")

        if chatserverRoom == k:
            global chatip
            break


chat = ChatListener(username, chatserverRoom)
chat.daemon = True
chat.start()
while True:
    msg = input()
    client.send(msg.encode("utf-8"))
    if msg == "/exit":
        print("Bye bye")
        sys.exit()