import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.connect(("10.20.40.191", 8005))
client.send(b"Hello from Elvis")

# time.sleep(1)

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(("0.0.0.0", 8005))
msg = server.recvfrom(255)
print(msg)