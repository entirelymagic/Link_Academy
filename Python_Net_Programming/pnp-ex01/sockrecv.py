import socket
import time

sSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sSocket.bind(("0.0.0.0",8005))
sSocket.listen()
print("Listening for connection: ")
# Socket accept a connection and an address
conn, addr = sSocket.accept() 

print("Connection received from ", addr)
data = conn.recv(1024)
print("Message from client: \n")
print(data)
conn.close()
sSocket.close()