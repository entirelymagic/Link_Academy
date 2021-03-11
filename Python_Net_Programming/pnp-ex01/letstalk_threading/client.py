import socket
import threading
import sys
import os
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
rooms = {}


class ChatListener(threading.Thread):
    username = ""

    def __init__(self, username, ip):
        super().__init__()
        self.username = username
        self.ip = ip

    def run(self):
        client.connect((self.ip, 8005))
        client.send(self.username.encode("utf-8"))
        while True:
            res = client.recv(1024).decode("utf-8")
            if res != "":
                print(f"\r\n{res}")
                print("Enter message: ", end="", flush=True)


username = input("Enter username: ")


class AdvertiserClient(threading.Thread):
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


adv = AdvertiserClient()
adv.daemon = True
adv.start()

chat_ip = None
running = True

while running:
    os.system('cmd /c "cls"')
    print("Available chat rooms: \n")
    rooms_available = {}
    counter = 0
    for k, v in rooms.items():
        rooms_available[counter] = k
        counter += 1
        print(f"Chat server {counter} on address: {k} available on port {v}")
        chat_server_room = input("Which room you would like to join?"
                                 "Select the number of each address to join"
                                 "Enter your option here: ")
        if chat_server_room == k:
            chat_ip = chat_server_room
            running = False

chat = ChatListener(username, chat_ip)
chat.daemon = True
chat.start()
while True:
    # print("Enter message: ")
    msg = input()

    client.send(msg.encode("utf-8"))
    if msg == "/exit":
        print("Bye bye")
        sys.exit()
        break
