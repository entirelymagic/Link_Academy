import socket
import threading
import time


def broadcast(msg):
    for user, sock in users.items():
        sock.send(msg.encode("utf-8"))


class Advertiser(threading.Thread):
    """A class that can see all the servers from the network and post them"""
    client = None

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        super().__init__()

    def run(self):
        while True:
            print("Advertising broadcast Sent")
            self.client.connect(("255.255.255.255", 8005))
            self.client.send(b"8005")
            time.sleep(5)


class ChatListener(threading.Thread):
    username = ""
    conn = None

    def __init__(self, username, conn):
        super().__init__()
        self.username = username
        self.conn = conn

    def run(self):
        while True:
            msg = self.conn.recv(1024).decode("utf-8")
            if msg == "/exit":
                del users[self.username]
                self.conn.close()
                broadcast(f"User {self.username} left the room")
                print(f"User {self.username} left")
                break
            else:
                print(f"User {self.username} say {msg}")
                broadcast(f"{self.username}: {msg}")


def accept(sock):
    conn, addr = sock.accept()
    # conn.setblocking(True)
    username = conn.recv(1024).decode("utf-8")
    # conn.setblocking(False)
    users[username] = conn

    # instantiate the class
    chat = ChatListener(username, conn)
    chat.daemon = True  # kill all sub threads
    chat.start()

    print(f"User {username} has entered room")
    broadcast(f"User {username} has entered room")


# Dict to hold connected users
users = {}

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ss.bind(("0.0.0.0", 8005))
ss.listen()
print("Chat server running...")

adv = Advertiser()
adv.daemon = True
adv.start()

while True:
    accept(ss)
